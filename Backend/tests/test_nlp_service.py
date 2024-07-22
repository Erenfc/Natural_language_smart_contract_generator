import unittest
from app.services.nlp_service import process_nlp_request

class TestNLPService(unittest.TestCase):
    def test_process_nlp_request(self):
        description = "Create a smart contract that transfers tokens."
        result = process_nlp_request(description)
        self.assertIn("contract", result)

if __name__ == '__main__':
    unittest.main()
