import pytest
import requests

class TestRegistrationExtra:
    def test_register_existing_username(self, base_url):
        """ניסיון להירשם עם שם משתמש שכבר קיים אמור להיכשל"""
        payload = {"username": "existing_user", "password": "StrongPass123", "email": "exist@example.com"}
        resp = requests.post(f"{base_url}/register", json=payload)
        assert resp.status_code in [400, 409]

    @pytest.mark.parametrize("password", ["123456", "password", "qwerty"])
    def test_register_with_common_passwords(self, base_url, password):
        """בדיקה שסיסמאות נפוצות וחלשות לא מתקבלות"""
        payload = {"username": f"user_{password}", "password": password, "email": f"{password}@test.com"}
        resp = requests.post(f"{base_url}/register", json=payload)
        assert resp.status_code in [400, 422]
