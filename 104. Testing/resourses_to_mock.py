import requests as requests

URL = "https://google.com"


class ThirdPartyAPI:
    def fetch_api(self):
        resp = requests.get(URL)
        if resp.status_code == 200:
            return "JSON real object"
        else:
            return "None"


def fetch_api_function():
    resp = requests.get(URL)
    if resp.status_code == 200:
        return "JSON real object"
    else:
        return "None"
