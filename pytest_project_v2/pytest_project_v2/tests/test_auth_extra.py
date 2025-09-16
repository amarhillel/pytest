import pytest
import requests

class TestAuthExtra:
    def test_login_with_wrong_content_type(self, base_url):
        """בודק מה קורה אם שולחים בקשה עם Content-Type שגוי"""
        url = f"{base_url}/login"
        headers = {"Content-Type": "text/plain"}
        resp = requests.post(url, data="username=test&password=1234", headers=headers)
        assert resp.status_code in [400, 415]

    def test_login_with_spaces_in_username(self, base_url):
        """בודק האם הרווחים בתחילת/סוף שם המשתמש נחתכים או נחשבים"""
        url = f"{base_url}/login"
        payload = {"username": "   testuser   ", "password": "correctpassword"}
        resp = requests.post(url, json=payload)
        assert resp.status_code in [200, 401, 400]

    def test_access_with_expired_or_invalid_token(self, base_url):
        """בודק שהמערכת מחזירה 401 כשמנסים עם טוקן לא תקף או שפג תוקף"""
        url = f"{base_url}/profile"
        headers = {"Authorization": "Bearer invalid_or_expired_token"}
        resp = requests.get(url, headers=headers)
        assert resp.status_code in [401, 403]
