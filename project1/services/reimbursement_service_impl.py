from entities.reimbursement import Reimbursement
from services.reimbursement_service import ReimbursementService
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

class ReimbursementServiceImpl(ReimbursementService):

    def __init__(self, reimbursement_dao: ReimbursementDao):
        self.reimbursement_dao = reimbursement_dao

    def retrieve_reimbursements(self, k_id: str):
        return self.reimbursement_dao.get_all_reimbursements(k_id)

    def submit_reimbursement(self, reimbursement: Reimbursement):
        return self.reimbursement_dao.create_reimbursement(reimbursement)

    def adjust_request(self, r_id: str, status: str, message: str):
        return self.reimbursement_dao.edit_reimbursement(r_id, status, message)

    def get_reason_stats(self, k_id: str):
        return self.reimbursement_dao.amounts_by_reason_by_knight(k_id)
