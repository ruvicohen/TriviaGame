import requests

def get_trivia_from_api(url):
    response = requests.get(url)
    return response.json()