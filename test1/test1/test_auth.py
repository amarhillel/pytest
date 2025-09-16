import pytest
import requests

class TestAuth:
    @pytest.mark.parametrize("username,password,expected_status", [
        ("testuser", "correctpassword", 200),
        ("wronguser", "correctpassword", 401),
        ("testuser", "wrongpassword", 401),
        ("", "", 400),
    ])
    def test_login_cases(self, base_url, username, password, expected_status):
        url = f"{base_url}/login"
        payload = {"username": username, "password": password}
        response = requests.post(url, json=payload)
        assert response.status_code == expected_status

    def test_login_sql_injection(self, base_url):
        url = f"{base_url}/login"
        payload = {"username": "' OR '1'='1", "password": "' OR '1'='1"}
        response = requests.post(url, json=payload)
        assert response.status_code in [400, 401, 403]
