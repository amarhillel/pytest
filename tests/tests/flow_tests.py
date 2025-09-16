import requests

def test_login_then_access_profile_then_logout():
    base_url = "http://10.0.0.1/api"
    login = requests.post(f"{base_url}/login", json={"username": "testuser", "password": "correctpassword"})
    assert login.status_code == 200
    token = login.json().get("token")

    headers = {"Authorization": f"Bearer {token}"}
    profile = requests.get(f"{base_url}/profile", headers=headers)
    assert profile.status_code == 200

    logout = requests.post(f"{base_url}/logout", headers=headers)
    assert logout.status_code in [200, 204]

