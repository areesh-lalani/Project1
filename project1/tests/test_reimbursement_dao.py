from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres
from entities.reimbursement import Reimbursement


reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()

test_reimbursement = Reimbursement(0, 1000, "Ale", None, None, 1)


def test_create_reimbursement():
    reimbursement_dao.create_reimbursement(test_reimbursement)
    assert test_reimbursement.reimbursement_id != 0

def test_get_all_reimbursements():
    assert len(reimbursement_dao.get_all_reimbursements(2)) > 1

def test_edit_reimbursement():
    assert test_reimbursement.status != reimbursement_dao.edit_reimbursement(str(test_reimbursement.reimbursement_id), "Denied", "For the Test")

def test_amount_by_reason():
    assert len(reimbursement_dao.amounts_by_reason_by_knight(2)) != 0

