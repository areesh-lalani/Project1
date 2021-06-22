from entities.reimbursement import Reimbursement
from abc import ABC, abstractmethod

class ReimbursementDao(ABC):

    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement)-> Reimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements(self, k_id: str):
        pass

    @abstractmethod
    def edit_reimbursement(self, r_id: str, status: str, message: str):
        pass

    @abstractmethod
    def amounts_by_reason_by_knight(self, k_id: int):
        pass
