# Pytest Project – API Testing Example

This project contains organized API tests written in **pytest** and **requests**.
The tests are grouped by functionality into separate files.

## 📂 Structure

- **conftest.py** → Fixtures (base_url, tokens, headers, thresholds).
- **tests/**
  - **test_auth.py** → Basic login tests (valid/invalid, SQL injection).
  - **test_profile.py** → Profile access with/without token.
  - **test_authorization.py** → Admin vs normal user access.
  - **test_flow.py** → Full flow: login → profile → logout.
  - **test_performance.py** → Response time tests with thresholds.
  - **test_errors.py** → Not found (404), reset password checks.
  - **test_registration.py** → Registration with valid/invalid inputs.
  - **test_registration_email_simple.py** → Registration enforcing email presence.

## ▶️ How to run

1. Install dependencies:
   ```bash
   pip install pytest requests
   ```

2. Run all tests:
   ```bash
   pytest -v
   ```

3. Run a specific file:
   ```bash
   pytest tests/test_auth.py -v
   ```

4. Run a single test by keyword:
   ```bash
   pytest -k "test_login_cases" -v
   ```

---
✨ Use this project as a starting point to practice API testing in interviews.
