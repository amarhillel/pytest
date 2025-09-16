import requests

def test_successful_registration():
    url = "http://10.0.0.1/api/register"
    payload = {
        "username": "newuser123",
        "password": "StrongPass123",
        "email": "test@example.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201

import pytest
import requests

@pytest.mark.parametrize("payload, expected_status", [
    ({"username": "newuser"}, 400),
    ({"username": "weakuser", "password": "123", "email": "weak@example.com"}, 400),
    ({"username": "bademailuser", "password": "GoodPass123", "email": "not-an-email"}, 400),
])
def test_registration_cases(payload, expected_status):
    url = "http://10.0.0.1/api/register"
    response = requests.post(url, json=payload)
    assert response.status_code == expected_status

