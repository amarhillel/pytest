import requests

def test_admin_access_with_user_token():
    login_url = "http://10.0.0.1/api/login"
    admin_url = "http://10.0.0.1/api/admin"
    login = requests.post(login_url, json={"username": "testuser", "password": "correctpassword"})
    token = login.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(admin_url, headers=headers)
    assert response.status_code == 403

import requests

def test_admin_access_with_admin_token():
    login_url = "http://10.0.0.1/api/login"
    admin_url = "http://10.0.0.1/api/admin"
    login = requests.post(login_url, json={"username": "adminuser", "password": "adminpassword"})
    token = login.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(admin_url, headers=headers)
    assert response.status_code == 200

