import requests

def get(apiURL):
    response = requests.get(apiURL);
    if(response.status_code  == 200):
        return response.json()
    else:
        return f"Bad request detected: {response.status_code }"
    