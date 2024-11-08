import allure

from tests.base_test import BaseTest


class TestAPIBreeds(BaseTest):

    def get_breeds(self, params=None, **kwargs):
        return self.base_get(endpoint="breeds", params=params, **kwargs)

    @allure.title("Successfully retrieves a list of cat breeds")
    def test_get_breeds_list(self):
        response = self.get_breeds()
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert isinstance(data["data"], list), "'data' field should be a list"
        for breed in data["data"]:
            assert "breed" in breed, "Each breed should contain the 'breed' key"
            assert "country" in breed, "Each breed should contain the 'country' key"
            assert "origin" in breed, "Each breed should contain the 'origin' key"
            assert "coat" in breed, "Each breed should contain the 'coat' key"
            assert "pattern" in breed, "Each breed should contain the 'pattern' key"

    @allure.title("Limit parameter: Check the number of returned breeds")
    def test_get_breeds_with_limit(self):
        limit = 1
        response = self.get_breeds(params={"limit": limit})
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        assert len(data["data"]) == limit, f"Expected {limit} breeds in response"

    @allure.title("Limit parameter: Check the number of returned breeds")
    def test_get_breeds_with_negative_limit(self):
        limit = -1
        response = self.get_breeds(params={"limit": limit})
        assert response.status_code != 200, "Expected error message"
        data = response.json()
        assert "error" in data or response.status_code == 404, "Expected error message or status code 404"

    @allure.title("Test that breeds pagination works and there are no duplicate entries")
    def test_breeds_pagination(self):
        response_page_1 = self.get_breeds(params={"limit": 5, "page": 1})
        response_page_2 = self.get_breeds(params={"limit": 5, "page": 2})
        assert response_page_1.status_code == 200 and response_page_2.status_code == 200
        data_page_1 = {breed["breed"] for breed in response_page_1.json()["data"]}
        data_page_2 = {breed["breed"] for breed in response_page_2.json()["data"]}
        assert not data_page_1.intersection(data_page_2), "Duplicate breeds found across pages"

    @allure.title("Test that an extremely large limit does not crash the API and returns a reasonable number of results")
    def test_breeds_with_large_limit(self):
        response = self.get_breeds(params={"limit": 1000})
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert len(data["data"]) <= 100, "Returned more than the reasonable maximum records"