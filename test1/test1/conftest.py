import pytest
import requests

BASE_URL = "http://10.0.0.1/api"
PERF_THRESHOLD_SECONDS = 3.0

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL.rstrip("/")

@pytest.fixture(scope="session")
def creds_user():
    return {"username": "testuser", "password": "correctpassword"}

@pytest.fixture(scope="session")
def creds_admin():
    return {"username": "adminuser", "password": "adminpassword"}

@pytest.fixture(scope="session")
def login_token(base_url, creds_user):
    resp = requests.post(f"{base_url}/login", json=creds_user)
    assert resp.status_code == 200, f"Login failed: {resp.text}"
    token = resp.json().get("token")
    assert token, "No token in login response"
    return token

@pytest.fixture(scope="session")
def admin_token(base_url, creds_admin):
    resp = requests.post(f"{base_url}/login", json=creds_admin)
    assert resp.status_code == 200, f"Admin login failed: {resp.text}"
    token = resp.json().get("token")
    assert token, "No admin token in login response"
    return token

@pytest.fixture
def auth_headers(login_token):
    return {"Authorization": f"Bearer {login_token}"}

@pytest.fixture
def admin_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}

@pytest.fixture(scope="session")
def perf_threshold_seconds():
    return PERF_THRESHOLD_SECONDS
