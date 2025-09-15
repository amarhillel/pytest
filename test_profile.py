class TestProfile:
    def test_profile_unauthorized(self, api, assert_status):
        resp = api("GET", "/profile")
        assert_status(resp, 401)

    def test_profile_with_token(self, api, auth_headers, assert_status):
        resp = api("GET", "/profile", headers=auth_headers)
        assert_status(resp, 200)