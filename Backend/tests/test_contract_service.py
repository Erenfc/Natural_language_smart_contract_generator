import unittest
from app.services.contract_service import generate_smart_contract
from app import db
from app.models import SmartContractRequest

class TestContractService(unittest.TestCase):
    def test_generate_smart_contract(self):
        description = "Create a smart contract that handles token transfers."
        contract_code = generate_smart_contract(description)
        self.assertIn("contract", contract_code)

        request_entry = SmartContractRequest.query.filter_by(description=description).first()
        self.assertIsNotNone(request_entry)
        self.assertEqual(request_entry.description, description)
        self.assertEqual(request_entry.contract_code, contract_code)

if __name__ == '__main__':
    unittest.main()
