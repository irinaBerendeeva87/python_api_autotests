
from tests.base_test import BaseTest

class TestAPIFact(BaseTest):

    def get_fact(self, params=None, **kwargs):
        return self.base_get(endpoint="fact", params=params, **kwargs)

    #Test retrieving a random cat fact
    def test_get_fact(self):
        response = self.get_fact()
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert "fact" in data, "Response should contain the 'fact' key"
        assert "length" in data, "Response should contain the 'length' key"
        assert isinstance(data["fact"], str), "'fact' field should be a string"
        assert isinstance(data["length"], int), "'length' field should be an integer"