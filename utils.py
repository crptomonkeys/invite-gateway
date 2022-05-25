import requests

class Disc:
    def __init__(
        self,
        server="127.0.0.1",
    ):
        self.limit = 100
        self.server = server
        self.url_base = f"http://{self.server}:8001"
    
    def create_invite(
        self,
        srv_id:int,
    ) -> requests.models.Response:
        return requests.get(f'{self.url_base}/create_invite?srvid={srv_id}')
    