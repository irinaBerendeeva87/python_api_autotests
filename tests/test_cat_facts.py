import allure

from base_test import BaseTest

class TestAPIFacts(BaseTest):

    def get_facts(self, params=None, **kwargs):
        return self.base_get(endpoint="facts", params=params, **kwargs)

    @allure.title("Successfully retrieves a list of cat facts")
    def test_get_list_facts(self):
        response = self.get_facts()
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert "data" in data, "Response should contain the 'data' key"
        assert isinstance(data["data"], list), "'data' field should be a list"
        for fact in data["data"]:
            assert "fact" in fact, "Each fact should contain the 'fact' key"
            assert "length" in fact, "Each fact should contain the 'length' key"

    @allure.title("Check limit parameter in GET /facts")
    def test_get_list_facts_with_limit(self):
        limit = 1
        response = self.get_facts( params={"limit": limit})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert len(data["data"]) == limit, f"Expected {limit} facts in response"

    @allure.title("Check max_length parameter in GET /facts")
    def test_get_list_facts_with_max_length(self):
        max_length = 50
        response = self.get_facts(params={"max_length": max_length})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        for fact in data["data"]:
            assert len(fact["fact"]) <= max_length, f"Fact length should not exceed {max_length}"

    @allure.title("Check pagination with limit and page parameters")
    def test_get_facts_with_pagination(self):
        limit, page = 3, 2
        response = self.get_facts(params={"limit": limit, "page": page})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert len(data["data"]) == limit, f"Expected {limit} facts on page {page}"