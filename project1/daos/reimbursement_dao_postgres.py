from entities.reimbursement import Reimbursement
from daos.reimbursement_dao import ReimbursementDao
from utils.connection_util import connection

class ReimbursementDaoPostgres(ReimbursementDao):

    def create_reimbursement(self, reimbursement: Reimbursement)-> Reimbursement:
        sql = """insert into reimbursement (amount, reason, status, message, k_id) values (%s,%s,%s,%s,%s) returning reimbursement_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.amount, reimbursement.reason, reimbursement.status,
                             reimbursement.message, reimbursement.k_id))
        connection.commit()
        r_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = r_id
        return reimbursement

    def get_all_reimbursements(self, k_id: int):
        sql = """select * from reimbursement where k_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [k_id])
        connection.commit()
        results = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in results:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def edit_reimbursement(self, r_id: str, status: str, message: str):
        sql = """update reimbursement set status = %s, message = %s where reimbursement_id = %s returning status"""
        cursor = connection.cursor()
        cursor.execute(sql, (status, message, r_id))
        connection.commit()
        return cursor.fetchone()[0]

    def amounts_by_reason_by_knight(self, k_id: int):
        sql = """select reason, sum(amount) from reimbursement where k_id = %s group by reason """
        cursor = connection.cursor()
        cursor.execute(sql, [k_id])
        connection.commit()
        results = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in results:
            reimbursement_list.append(reimbursement)
        return reimbursement_list






