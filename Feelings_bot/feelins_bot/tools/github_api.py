from typing import Union

import aiohttp

from user_classes import Github_user


class Github_handler(Github_user):
    def __init__(self):
        super().__init__()
        self.headers = {'Authorization': f"token {self.token}"}

    def __str__(self):
        return "Github handler"

    async def create_gist(self, content, file_name: str = "main.py",
                          description: str = "gist") -> Union[str, tuple]:
        payload: dict = {
            "description": description,
            "files": {file_name: {"content": content}},
            "public": True
        }
        async with aiohttp.ClientSession() as session:
            response = await session.post(self.api_gist_url,
                                          headers=self.headers, json=payload)
        if response.status == 201:
            return (await response.json())["html_url"]
        return "Error!", response.status

    async def create_repo(self, name: str, priv: bool = False,
                          description: str = "") -> str:
        payload: dict = {
            "name": name,
            "description": description,
            "private": priv,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        async with aiohttp.ClientSession() as session:
            response = await session.post(self.api_repo_url,
                                          headers=self.headers, json=payload)
        return (await response.json())["html_url"]

    async def delete_repo(self, name: str) -> None:
        url: str = f"https://api.github.com/repos/{self.username}/{name}"
        async with aiohttp.ClientSession() as session:
            await session.delete(url, headers=self.headers)
