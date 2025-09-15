import pytest

class TestPerformance:
    @pytest.mark.parametrize("endpoint,method,use_auth", [
        ("/login", "POST", False),
        ("/profile", "GET", True),
    ])
    def test_page_load_time(self, api, auth_headers, perf_threshold_seconds, endpoint, method, use_auth):
        kwargs = {}
        if use_auth:
            kwargs["headers"] = auth_headers
        if method == "POST" and endpoint == "/login":
            kwargs["json"] = {"username": "testuser", "password": "correctpassword"}

        resp = api(method, endpoint, **kwargs)
        load_time = resp.elapsed.total_seconds()
        print(f"\n{method} {endpoint} took {load_time:.2f}s (threshold {perf_threshold_seconds:.2f}s)")
        assert load_time < perf_threshold_seconds, f"⚠️ {endpoint} too slow: {load_time:.2f}s"