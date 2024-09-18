import requests

def get_users_from_api(url):
    response = requests.get(url)
    return response.json()