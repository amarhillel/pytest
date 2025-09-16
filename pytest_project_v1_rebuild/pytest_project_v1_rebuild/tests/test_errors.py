import requests

class TestErrors:
    def test_not_found(self, base_url):
        url = f"{base_url}/does-not-exist"
        response = requests.get(url)
        assert response.status_code == 404

    def test_password_reset_request(self, base_url):
        url = f"{base_url}/password-reset"
        response = requests.post(url, json={"email": "test@example.com"})
        assert response.status_code == 200
