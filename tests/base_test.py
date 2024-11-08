import requests

BASE_URL = "https://catfact.ninja/"

class BaseTest:

    def base_get(self,endpoint: str, params=None, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        return requests.get(url, params, **kwargs)