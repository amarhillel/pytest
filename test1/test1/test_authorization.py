import requests

class TestAuthorization:
    def test_admin_access_with_user_token(self, base_url, auth_headers):
        url = f"{base_url}/admin"
        response = requests.get(url, headers=auth_headers)
        assert response.status_code == 403

    def test_admin_access_with_admin_token(self, base_url, admin_headers):
        url = f"{base_url}/admin"
        response = requests.get(url, headers=admin_headers)
        assert response.status_code == 200
