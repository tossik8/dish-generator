import unittest, json
from fastapi.testclient import TestClient
from app import app

# Create a TestClient instance for testing
client = TestClient(app)
test_input=[{"name":"bread","quantity":""},{"name":"onion","quantity":""},{"name":"apples","quantity":"2"}]
expected_output=[
        {
            "name": "Toast",
            "description": "Bread, Crunchy",
            "image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
            "ingredients": [
                {"name": "Sliced Bread", "quantity": "4 pieces"},
                {"name": "Butter", "quantity": "to taste"}
            ],
            "instructions": [
                "Put bread in toaster",
                "Wait until you smell something burning",
                "Pop out the half burnt toast",
                "Apply Butter"
            ]
        },
        {
            "name": "Anything",
            "description": "Absolutely Anything",
            "image": "https://www.fuller.edu/wp-content/uploads/2022/11/secondary-banner-placeholder.jpg",
            "ingredients": [
                {"name": "Phone", "quantity": "1"},
                {"name": "Internet", "quantity": "decent bandwidth"},
                {"name": "Credit Card", "quantity": "Just 1 but with enough limit"}
            ],
            "instructions": [
                "Install UberEats",
                "Order whatever you want",
                "Pay with credit card",
                "Wait for Delivery",
                "Enjoy"
            ]
        }
    ]
class TestAPI(unittest.TestCase):
    def test_check_resp(self):
        response = client.post("/gen_recipies/", json=test_input)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.dumps(response.json()),json.dumps(expected_output))