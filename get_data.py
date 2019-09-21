import requests
import json


# Uses the API key method to connect
# https://www.campaignmonitor.com/api/getting-started/#authenticating-api-key
def get_data(url, user, pwd):
    _conn = requests.get(url, auth=('{}'.format(user), '{}'.format(pwd)))
    _data = json.loads(_conn.text)
    return _data
