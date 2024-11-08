import requests

from tests.base_test import BaseTest

class TestAPIFacts(BaseTest):

    def get_facts(self, params=None, **kwargs):
        return self.base_get(endpoint="facts", params=params, **kwargs)

    #Successfully retrieves a list of cat facts
    def test_get_list_facts(self):
        response = self.get_facts("facts")
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert "data" in data, "Response should contain the 'data' key"
        assert isinstance(data["data"], list), "'data' field should be a list"
        for fact in data["data"]:
            assert "fact" in fact, "Each fact should contain the 'fact' key"
            assert "length" in fact, "Each fact should contain the 'length' key"