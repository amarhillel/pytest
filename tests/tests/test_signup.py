import time
import pytest

@pytest.mark.parametrize(
    "password, expected_codes, note",
    [
        ("123", {400, 422}, "too short numeric"),
        ("abc", {400, 422}, "too short letters"),
        ("pass", {400, 422}, "less than 8 chars"),
    ],
)
def test_signup_rejects_weak_passwords(http, signup_url, password, expected_codes, note):
    """
    בדיקה: הרשמה עם סיסמאות חלשות צריכה להיכשל (ולידציה).
    """
    # שם ייחודי כדי לא להתנגש בהרצות חוזרות
    username = f"user_{int(time.time())}"
    payload = {"username": username, "password": password}
    r = http.post(signup_url, json=payload, timeout=10)
    assert r.status_code in expected_codes, f"{note}: got {r.status_code}, expected {expected_codes}"
