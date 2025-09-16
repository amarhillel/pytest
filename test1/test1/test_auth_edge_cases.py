import pytest
import requests

REQUEST_TIMEOUT = 5

class TestAuthEdgeCases:

    @pytest.mark.parametrize("payload, expected", [
        ({"username": "testuser", "password": "correctpassword"}, 200),
        ({"username": "no_such_user_123", "password": "whatever"}, 401),
        ({"username": "testuser", "password": "wrongpassword"}, 401),
        ({"username": "", "password": ""}, 400),
        ({"username": "testuser"}, 400),
        ({"password": "correctpassword"}, 400),
        ({"username": "<script>alert(1)</script>", "password": "123456"}, 400),
        ({"username": "testuser", "password": "123"}, 400),
        ({"username": "testuser", "password": "x" * 300}, [400, 413]),
        ({"username": "testuser", "password": None}, 400),
        ({"username": None, "password": None}, 400),
        ({"username": "testuser", "password": 12345}, 400),
        ({"username": "' OR '1'='1", "password": "' OR '1'='1"}, [400, 401, 403]),
        ({"username": "TESTUSER", "password": "correctpassword"}, [200, 401]),
        ({"username": "lockeduser", "password": "correctpassword"}, [403, 401]),
        ({"username": "testuser", "password": "P@$$w0rd!"}, 200),
        ({"username": "testuser", "password": "пароль🔥"}, [200, 401]),
    ])
    def test_login_various_edge_cases(self, base_url, payload, expected):
        url = f"{base_url}/login"
        resp = requests.post(url, json=payload, timeout=REQUEST_TIMEOUT)
        allowed = expected if isinstance(expected, (list, tuple, set)) else (expected,)
        assert resp.status_code in allowed, (
            f"Unexpected status for payload={payload!r}: got {resp.status_code}, body={resp.text}"
        )

    def test_many_failed_attempts_may_lock_or_rate_limit(self, base_url):
        url = f"{base_url}/login"
        payload = {"username": "ratelimit_user", "password": "wrongpassword"}
        last_resp = None
        for i in range(8):
            resp = requests.post(url, json=payload, timeout=REQUEST_TIMEOUT)
            last_resp = resp
            if resp.status_code in (429, 403):
                break
        assert last_resp is not None, "No response from server during rate-limit test"
        assert last_resp.status_code in (401, 429, 403), (
            f"Expected 401/429/403 after many failed attempts, got {last_resp.status_code}, body={last_resp.text}"
        )

    def test_login_returns_token_on_success(self, base_url, creds_user):
        url = f"{base_url}/login"
        resp = requests.post(url, json=creds_user, timeout=REQUEST_TIMEOUT)
        assert resp.status_code == 200, f"Login failed: {resp.status_code}, body={resp.text}"
        try:
            data = resp.json()
        except ValueError:
            pytest.fail(f"Expected JSON response, got: {resp.text}")
        assert isinstance(data, dict), f"Expected JSON object, got: {data!r}"
        assert "token" in data and data["token"], f"No token in response body: {data!r}"
