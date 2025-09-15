class TestAuthorization:
    def test_admin_access_with_user_token(self, api, auth_headers, assert_status):
        resp = api("GET", "/admin", headers=auth_headers)
        assert_status(resp, 403)

    def test_admin_access_with_admin_token(self, api, admin_headers, assert_status):
        resp = api("GET", "/admin", headers=admin_headers)
        assert_status(resp, 200)