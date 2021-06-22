from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres
from utils.connection_util import connection

class ReimbursementService(ABC):
    @abstractmethod
    def retrieve_reimbursements(self, k_id: str):
        pass

    @abstractmethod
    def submit_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def adjust_request(self, r_id: str, status: str, message: str):
        pass

    @abstractmethod
    def get_reason_stats(self, k_id: str):
        pass