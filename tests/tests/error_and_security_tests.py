import requests

def test_not_found():
    url = "http://10.0.0.1/api/does-not-exist"
    response = requests.get(url)
    assert response.status_code == 404

import requests

def test_forbidden_access():
    url = "http://10.0.0.1/api/admin"
    response = requests.get(url)
    assert response.status_code == 403

import requests

def test_password_reset_request():
    url = "http://10.0.0.1/api/password-reset"
    payload = {"email": "test@example.com"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200

