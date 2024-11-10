import allure

from base_test import BaseTest

class TestAPIFact(BaseTest):

    def get_fact(self, params=None, **kwargs):
        return self.base_get(endpoint="fact", params=params, **kwargs)

    @allure.title("Test retrieving a random cat fact")
    def test_get_fact(self):
        response = self.get_fact()
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert "fact" in data, "Response should contain the 'fact' key"
        assert "length" in data, "Response should contain the 'length' key"
        assert isinstance(data["fact"], str), "'fact' field should be a string"
        assert isinstance(data["length"], int), "'length' field should be an integer"

    @allure.title("Check max_length parameter")
    def test_get_random_fact_with_max_length(self):
        max_length = 50
        response = self.get_fact(params={"max_length": max_length})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert len(data["fact"]) <= max_length, f"Fact length should not exceed {max_length}"

    @allure.title("Check handling of invalid max_length value")
    def test_get_random_fact_with_max_length_zero_returns_empty(self):
        max_length = 0
        response = self.get_fact(params={"max_length": max_length})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert data == {}, f"Expected empty dictionary, got {data}"