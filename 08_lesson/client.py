import requests
from config import get_base_url, get_token


class YougileClient:
    def __init__(self):
        self.base_url = get_base_url()
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {get_token()}",
                "Content-Type": "application/json",
            }
        )

    def create_project(self, payload: dict):
        return self.session.post(
            f"{self.base_url}/api-v2/projects",
            json=payload,
        )

    def get_project(self, project_id: str):
        return self.session.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
        )

    def update_project(self, project_id: str, payload: dict):
        return self.session.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
        )
