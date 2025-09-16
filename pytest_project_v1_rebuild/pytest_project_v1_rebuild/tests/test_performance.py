import pytest
import requests

class TestPerformance:
    @pytest.mark.parametrize("endpoint,method,use_auth", [
        ("/login", "POST", False),
        ("/profile", "GET", True),
    ])
    def test_page_load_time(self, base_url, auth_headers, perf_threshold_seconds, endpoint, method, use_auth):
        url = f"{base_url}{endpoint}"
        kwargs = {}
        if use_auth:
            kwargs["headers"] = auth_headers
        if method == "POST" and endpoint == "/login":
            kwargs["json"] = {"username": "testuser", "password": "correctpassword"}
        response = requests.request(method, url, **kwargs)
        load_time = response.elapsed.total_seconds()
        assert load_time < perf_threshold_seconds, f"{endpoint} too slow: {load_time:.2f}s"
