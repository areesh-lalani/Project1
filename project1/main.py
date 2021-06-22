from entities.reimbursement import Reimbursement
from utils.connection_util import connection
from flask import Flask, request, jsonify
from flask_cors import CORS
from daos.reimbursement_dao import ReimbursementDao
from daos.knight_dao import KnightDao
from daos.knight_dao_postgres import KnightDaoPostgres
from daos.lord_dao import LordDao
from daos.lord_dao_postgres import LordDaoPostgres
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres
from services.knight_service import KnightService
from services.knight_service_impl import KnightServiceImpl
from services.lord_service import LordService
from services.lord_service_impl import LordServiceImpl
from services.reimbursement_service import ReimbursementService
from services.reimbursement_service_impl import ReimbursementServiceImpl
import json
import logging

app: Flask = Flask(__name__)
CORS(app)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')


knight_dao: KnightDao = KnightDaoPostgres()
knight_service: KnightService = KnightServiceImpl(knight_dao)

lord_dao: LordDao = LordDaoPostgres()
lord_service: LordService = LordServiceImpl(lord_dao)

reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()
reimbursement_service: ReimbursementService = ReimbursementServiceImpl(reimbursement_dao)

@app.route("/knights", methods = ["POST"])
def login():
    body = request.json
    sql = """ select * from knight where user_name = %s"""
    cursor = connection.cursor()
    cursor.execute(sql, [body["userName"]])
    record = cursor.fetchone()
    try:
        if body["passWord"] == record[6]:
            return "pass", 201
    except TypeError:
        return "fail", 200

@app.route("/lords", methods = ["POST"])
def lord_login():
    body = request.json
    sql = """ select * from lord where user_name = %s"""
    cursor = connection.cursor()
    cursor.execute(sql, [body["userName"]])
    record = cursor.fetchone()
    try:
        if body["passWord"] == record[5]:
            return "pass", 201
    except TypeError:
        return "fail", 200

@app.route("/knights/<username>", methods = ["GET"])
def get_knight(username: str):
    knight = knight_service.retrieve_knight_by_user(username)
    result = knight.as_json_dict()
    return jsonify(result)

@app.route("/lords/<username>", methods = ["GET"])
def get_lord(username: str):
    lord = lord_service.retrieve_lord_by_user(username)
    result = lord.as_json_dict()
    return jsonify(result)

@app.route("/knights/reimbursements/<k_id>", methods = ["GET"])
def get_reimbursements(k_id: str):
    reimbursements = reimbursement_service.retrieve_reimbursements(int(k_id))
    json_reimbursements = [r.as_json_dict() for r in reimbursements]
    return jsonify(json_reimbursements)

@app.route("/knights/reimbursements", methods = ["POST"])
def submit_reimbursement():
    body = request.json
    reimbursement = Reimbursement(0, body["amount"], body["reason"], "Under Consideration", "", body["kId"])
    reimbursement_service.submit_reimbursement(reimbursement).as_json_dict()
    return "Request Submitted", 201

@app.route("/lords/knights/<l_id>", methods = ["GET"])
def get_all_knights_by_lord(l_id: str):
    knights = knight_service.retrieve_knights_by_lord(int(l_id))
    return json.dumps(knights)

@app.route("/lords/reimbursements", methods = ["PATCH"])
def edit_request():
    body = request.json
    reimbursement_service.adjust_request(body["rId"], body["status"], body["message"])
    return body["status"], 201


@app.route("/lords/reimbursements/<k_id>", methods = ["GET"])
def get_reason_stats(k_id: str):
    reimbursements = reimbursement_service.get_reason_stats(int(k_id))
    return jsonify(reimbursements)

app.run()
