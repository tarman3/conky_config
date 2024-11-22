import subprocess

import requests
import json

ip_api_url = 'http://ip-api.com/json'
# id='nl-170068'

# command = f"nmcli c show {id}"
# direct_output = subprocess.check_output(command, shell=True)

# if b'GENERAL.STATE' in direct_output:

try:
    json_data = requests.get(ip_api_url, timeout=2).text
    # print(json_data)

    countryCode = json.loads(json_data)['countryCode']
    print(countryCode)
except Exception:
    pass
