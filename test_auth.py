import pytest

class TestAuth:
    @pytest.mark.parametrize("username,password,expected", [
        ("testuser", "correctpassword", 200),
        ("wronguser", "correctpassword", 401),
        ("testuser", "wrongpassword", 401),
        ("", "", 400),
    ])
    def test_login_cases(self, api, assert_status, username, password, expected):
        resp = api("POST", "/login", json={"username": username, "password": password})
        assert_status(resp, expected)

    @pytest.mark.parametrize("payload", [
        {"username": "' OR '1'='1", "password": "' OR '1'='1"},
        {"username": "<script>alert(1)</script>", "password": "x"},
    ])
    def test_login_attack_payloads(self, api, assert_status, payload):
        resp = api("POST", "/login", json=payload)
        assert_status(resp, [400, 401, 403])
        assert "token" not in resp.text