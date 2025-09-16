import pytest
import requests

@pytest.fixture
def login_url():
    return "http://10.0.0.1/api/login"

@pytest.mark.parametrize("username, password, expected_status", [
    ("testuser", "correctpassword", 200),
    ("wronguser", "correctpassword", 401),
    ("testuser", "wrongpassword", 401),
    ("", "", 400),
])
def test_login_cases(login_url, username, password, expected_status):
    payload = {"username": username, "password": password}
    response = requests.post(login_url, json=payload)
    assert response.status_code == expected_status

import requests

def test_login_sql_injection():
    url = "http://10.0.0.1/api/login"
    payload = {"username": "' OR '1'='1", "password": "' OR '1'='1"}
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 401, 403]

