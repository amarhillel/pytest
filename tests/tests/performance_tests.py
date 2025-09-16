import requests

def test_login_response_time():
    url = "http://10.0.0.1/api/login"
    payload = {"username": "testuser", "password": "correctpassword"}
    response = requests.post(url, json=payload)
    assert response.elapsed.total_seconds() < 2

import requests

def test_profile_response_time():
    login_url = "http://10.0.0.1/api/login"
    profile_url = "http://10.0.0.1/api/profile"
    login = requests.post(login_url, json={"username": "testuser", "password": "correctpassword"})
    token = login.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(profile_url, headers=headers)
    assert response.elapsed.total_seconds() < 2



import requests

def test_page_load_time():
    url = "http://10.0.0.1/api/products"  # או כל עמוד שתרצי לבדוק
    max_time = 3  # זמן מקסימלי שנחשב תקין (שניות)

    response = requests.get(url)
    load_time = response.elapsed.total_seconds()

    print(f"\nPage load time: {load_time:.2f} seconds")

    assert load_time < max_time, f"⚠️ Page load too slow! Took {load_time:.2f}s"


