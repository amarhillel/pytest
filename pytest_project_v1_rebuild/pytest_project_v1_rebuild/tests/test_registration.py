import pytest
import requests

class TestRegistration:
    @pytest.mark.parametrize("payload,expected", [
        ({"username": "newuser123", "password": "StrongPass123", "email": "test@example.com"}, 201),
        ({"username": "newuser"}, 400),
        ({"username": "weakuser", "password": "123", "email": "weak@example.com"}, 400),
        ({"username": "bademailuser", "password": "GoodPass123", "email": "not-an-email"}, 400),
    ])
    def test_registration_cases(self, base_url, payload, expected):
        url = f"{base_url}/register"
        response = requests.post(url, json=payload)
        assert response.status_code == expected
