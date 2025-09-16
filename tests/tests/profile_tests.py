import requests

def test_profile_unauthorized():
    url = "http://10.0.0.1/api/profile"
    response = requests.get(url)
    assert response.status_code == 401

import requests

def test_profile_with_token():
    login_url = "http://10.0.0.1/api/login"
    profile_url = "http://10.0.0.1/api/profile"
    payload = {"username": "testuser", "password": "correctpassword"}
    login = requests.post(login_url, json=payload)
    token = login.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(profile_url, headers=headers)
    assert response.status_code == 200

