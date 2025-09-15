# API Tests with Pytest

## 📦 Installation
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install pytest requests
   ```

## ▶️ Running Tests
From the project root (where the `tests/` folder is):

- Run **all tests**:
  ```bash
  pytest -q
  ```

- Run tests and show extra info:
  ```bash
  pytest -v
  ```

- Run only one file (example: authentication tests):
  ```bash
  pytest tests/test_auth.py -v
  ```

## 📂 Project Structure
```
tests/
├─ conftest.py          # Fixtures: base_url, tokens, headers, helpers
├─ test_auth.py         # Login tests (valid, invalid, SQL injection)
├─ test_registration.py # Registration tests
├─ test_profile.py      # Profile access with/without token
├─ test_authorization.py# User vs Admin access
├─ test_flow.py         # End-to-End flow (Login ➜ Profile ➜ Logout)
├─ test_performance.py  # Response time checks
└─ test_errors.py       # Error handling (404, password reset)
```

## 📝 Notes
- The base URL is set in `conftest.py` (`BASE_URL = "http://10.0.0.1/api"`). Change it if needed.
- Default test users:
  - Normal user: `testuser` / `correctpassword`
  - Admin user: `adminuser` / `adminpassword`
- Performance threshold: 3 seconds (can be adjusted in `conftest.py`).

Good luck 🍀 with your interview!