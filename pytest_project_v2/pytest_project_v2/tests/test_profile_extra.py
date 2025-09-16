import requests

class TestProfileExtra:
    def test_cannot_delete_profile(self, base_url, auth_headers):
        """בודק שקריאת DELETE לפרופיל לא מותרת ומחזירה 405"""
        url = f"{base_url}/profile"
        resp = requests.delete(url, headers=auth_headers)
        assert resp.status_code in [405, 403]

    def test_profile_does_not_leak_sensitive_fields(self, base_url, auth_headers):
        """בודק שהתשובה לא מכילה שדות רגישים כמו hash של הסיסמה"""
        url = f"{base_url}/profile"
        resp = requests.get(url, headers=auth_headers)
        if resp.status_code == 200:
            data = resp.json()
            assert "password" not in data
            assert "hash" not in data
