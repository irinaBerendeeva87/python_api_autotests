from tests.base_test import BaseTest


class TestAPIBreeds(BaseTest):

    def get_breeds(self, params=None, **kwargs):
        return self.base_get(endpoint="breeds", params=params, **kwargs)

    #Successfully retrieves a list of cat breeds"
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