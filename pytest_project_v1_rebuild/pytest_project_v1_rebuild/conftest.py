import pytest

# בסיס ה-URL של ה-API
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:5000"  # לשנות לפי השרת האמיתי

# טוקן של יוזר רגיל (מדמה לוגין תקין)
@pytest.fixture
def login_token():
    return "dummy_user_token"

# טוקן של אדמין
@pytest.fixture
def admin_token():
    return "dummy_admin_token"

# headers עם Authorization ליוזר רגיל
@pytest.fixture
def auth_headers(login_token):
    return {"Authorization": f"Bearer {login_token}"}

# headers עם Authorization לאדמין
@pytest.fixture
def admin_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}

# סף לבדיקות ביצועים (בשניות)
@pytest.fixture(scope="session")
def perf_threshold_seconds():
    return 2.0
