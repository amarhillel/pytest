import requests

class TestRegistrationEmailSimple:
    def test_register_without_email(self, base_url):
        # מנסה להירשם בלי אימייל בכלל → צריך להחזיר 400
        payload = {"username": "user_no_email", "password": "StrongPass123"}
        resp = requests.post(f"{base_url}/register", json=payload)
        assert resp.status_code == 400

    def test_register_with_invalid_email(self, base_url):
        # מנסה להירשם עם אימייל לא חוקי → צריך להחזיר 400
        payload = {"username": "user_bad_email", "password": "StrongPass123", "email": "not-an-email"}
        resp = requests.post(f"{base_url}/register", json=payload)
        assert resp.status_code == 400

    def test_register_with_valid_email(self, base_url):
        # מנסה להירשם עם אימייל חוקי → צריך להחזיר 201
        payload = {"username": "user_ok", "password": "StrongPass123", "email": "ok@example.com"}
        resp = requests.post(f"{base_url}/register", json=payload)
        assert resp.status_code == 201
