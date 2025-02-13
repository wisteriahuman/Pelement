import requests

SERVERURL = "http://127.0.0.1:8000/"

def get_all_player():
    response = requests.get(SERVERURL + "player/")
    return response.json()
