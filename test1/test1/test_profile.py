import requests

class TestProfile:
    def test_profile_unauthorized(self, base_url):
        url = f"{base_url}/profile"
        response = requests.get(url)
        assert response.status_code == 401

    def test_profile_with_token(self, base_url, auth_headers):
        url = f"{base_url}/profile"
        response = requests.get(url, headers=auth_headers)
        assert response.status_code == 200
