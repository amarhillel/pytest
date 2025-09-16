import pytest

@pytest.mark.parametrize(
    "payload, expected_codes, note",
    [
        # הצלחה
        ({"username": "valid_user", "password": "valid_pass"}, {200, 201}, "success"),
        # סיסמה שגויה
        ({"username": "valid_user", "password": "wrong_pass"}, {401, 403}, "wrong password"),
        # חסר סיסמה
        ({"username": "valid_user"}, {400}, "missing password"),
        # חסר שם משתמש
        ({"password": "some_pass"}, {400}, "missing username"),
    ],
)
def test_login_cases(http, login_url, payload, expected_codes, note):
    """
    טסט פרמטרי: בודק תרחישי לוגין שונים מול אותם fixtures.
    """
    r = http.post(login_url, json=payload, timeout=10)
    assert r.status_code in expected_codes, f"{note}: got {r.status_code}, expected {expected_codes}"
