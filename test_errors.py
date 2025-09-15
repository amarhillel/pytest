class TestErrors:
    def test_not_found(self, api, assert_status):
        resp = api("GET", "/does-not-exist")
        assert_status(resp, 404)

    def test_password_reset_request(self, api, assert_status):
        resp = api("POST", "/password-reset", json={"email": "test@example.com"})
        assert_status(resp, 200)