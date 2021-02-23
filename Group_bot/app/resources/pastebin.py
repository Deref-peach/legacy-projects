from typing import Dict, Union

import aiohttp

from user_classes import Pastebin_user


class Pastebin(Pastebin_user):
    """Class to pastebin API (see https://pastebin.com/api/)."""

    def __init__(self, paste_expire_date: str, paste_name: str, results_limit: int = 50):
        """Init.

        Args:
            paste_expire_date (str): sets the expiration date of your paste.
            paste_private (int): makes a paste public, unlisted or private,
                                public = 0, unlisted = 1, private = 2
            paste_name (str): will be the name / title of your paste.

            results_limit (int, optional): should be in range(1, 1001).Defaults to 50.

        """
        super().__init__()
        self.paste_expire_date: str = paste_expire_date
        self.paste_private: int = 0
        self.paste_name: str = paste_name
        self.results_limit: int = results_limit

        self.api_option: str = ""

    def __str__(self):
        """Most readly name."""
        return "Pastebin obj"

    async def get_post_response(self, data: Dict[str, Union[str, int]],
                                url: str) -> Union[str, tuple]:
        """Get response from server.

        Args:
            data (Dict[str, Union[str, int]]): data to post requests
            url (str): url to requests

        Returns
            Union[str, tuple]: response`s text

        """
        async with aiohttp.ClientSession() as ses:
            res = await ses.post(url, data=data)
        if res.status == 200:
            return await res.text()
        return "Error!", res.status, res.text()

    async def create_paste(self, code: str, paste_format: str):
        """Create new paste on pastebin.

        Args:
            code (str): code to paste
            paste_format (str): paste format # python

        """
        self.api_option = "paste"
        data: Dict[str, Union[str, int]] = {
            "api_option": self.api_option,
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,

            "api_paste_expire_date": self.paste_expire_date,
            "api_paste_private": self.paste_private,
            "api_paste_name": self.paste_name,
            "api_paste_format": paste_format,
            "api_paste_code": code,
        }
        return await self.get_post_response(data, self.post_url)

    async def get_user_publications(self,):
        """Return user publications on p-bin.

        Args:
            results_limit (int, optional): limit of count results user`s publications.
            Defaults to 50.

        """
        self.api_option = "list"
        data: Dict[str, Union[str, int]] = {
            "api_option": self.api_option,
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_results_limit": self.results_limit
        }
        return await self.get_post_response(data, self.post_url)

    async def delete_paste(self, paste_key: str):
        """Delete user`s paste.

        Args:
            paste_key (str): paste to delete key

        """
        self.api_option = "delete"
        data: dict = {
            "api_option": self.api_option,
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_paste_key": paste_key
        }
        return await self.get_post_response(data, self.post_url)

    async def get_user_settings(self):
        """Return user info and settings."""
        self.api_option = "userdetails"
        data: Dict[str, str] = {
            "api_option": self.api_option,
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
        }
        return await self.get_post_response(data, self.post_url)

    async def get_private_paste_rawdata(self, paste_key: str):
        """Get raw paste output of users pastes including 'private' pastes.

        Args:
            paste_key (str): key of paste to get content

        """
        self.api_option = "show_paste"
        data: dict = {
            "api_option": self.api_option,
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_paste_key": paste_key
        }
        return await self.get_post_response(data, self.raw_private)

    async def get_public_paste_rawdata(self, paste_key: str):
        """Get raw paste output of any 'public' & 'unlisted' pastes.

        Args:
            paste_key (str): key of paste to get content

        """
        async with aiohttp.ClientSession() as ses:
            res = await ses.post(self.raw_public + paste_key)
        if res.status == 200:
            return await res.text()
        return "Error!", res.status, res.text()
