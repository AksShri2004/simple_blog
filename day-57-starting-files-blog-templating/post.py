import requests

class Post:
    def __init__(self):
        self.request = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

