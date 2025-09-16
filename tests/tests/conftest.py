import os
import pytest
import requests

@pytest.fixture(scope="session", autouse=True)
def base_url():
    # אפשר לשנות בהרצה: BASE_URL=http://10.0.0.1 pytest -q
    return os.getenv("BASE_URL", "http://10.0.0.1").rstrip("/")

@pytest.fixture(scope="session")
def http():
    s = requests.Session()
    s.headers.update({"User-Agent": "pytest-login/1.0"})
    return s

@pytest.fixture(scope="session")
def login_url(base_url):
    return f"{base_url}/login"

@pytest.fixture(scope="session")
def valid_creds():
    # שנה לערכים אמיתיים אצלך או דרך ENV
    return {"username": os.getenv("API_USER", "valid_user"),
            "password": os.getenv("API_PASS", )}

@pytest.fixture(scope="session")
def signup_url(base_url):
    return f"{base_url}/signup"