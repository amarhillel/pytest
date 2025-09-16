import requests

def test_file_upload():
    url = "http://10.0.0.1/api/upload"
    files = {'file': ('test.txt', b'Hello world', 'text/plain')}
    response = requests.post(url, files=files)
    assert response.status_code == 200

