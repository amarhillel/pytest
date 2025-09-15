import pytest

class TestRegistration:
    @pytest.mark.parametrize("payload,expected", [
        ({"username": "newuser123", "password": "StrongPass123", "email": "test@example.com"}, 201),
        ({"username": "newuser"}, 400),
        ({"username": "weakuser", "password": "123", "email": "weak@example.com"}, 400),
        ({"username": "bademailuser", "password": "GoodPass123", "email": "not-an-email"}, 400),
    ])
    def test_registration_cases(self, api, assert_status, payload, expected):
        resp = api("POST", "/register", json=payload)
        assert_status(resp, expected)