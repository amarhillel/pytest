import requests

class TestErrorsExtra:
    def test_invalid_json_returns_400(self, base_url):
        """שולחים גוף בקשה לא חוקי (JSON שבור) ובודקים שמחזיר 400 ולא 500"""
        url = f"{base_url}/login"
        resp = requests.post(url, data="{bad json}")
        assert resp.status_code == 400
