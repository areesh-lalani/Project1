

class Reimbursement():
    def __init__(self, reimbursement_id: int, amount: int, reason: str, status: str, message: str, k_id: int):
        self.reimbursement_id = reimbursement_id
        self.amount = amount
        self.reason = reason
        self.status = status
        self.message = message
        self.k_id = k_id

    def as_json_dict(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "amount": self.amount,
            "reason": self.reason,
            "status": self.status,
            "message": self.message,
            "kId": self.k_id
        }

    