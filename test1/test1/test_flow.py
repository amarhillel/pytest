import requests

class TestFlow:
    def test_login_profile_logout_flow(self, base_url):
        login = requests.post(f"{base_url}/login", json={"username": "testuser", "password": "correctpassword"})
        assert login.status_code == 200, login.text
        token = login.json().get("token")
        assert token, "no token returned"

        headers = {"Authorization": f"Bearer {token}"}
        profile = requests.get(f"{base_url}/profile", headers=headers)
        assert profile.status_code == 200, profile.text

        logout = requests.post(f"{base_url}/logout", headers=headers)
        assert logout.status_code in [200, 204], logout.text
