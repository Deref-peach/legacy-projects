import os
from typing import Final

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Pastebin_user:
    """Pastebin User."""

    def __init__(self):
        """Config params.

        Args:
            api_user_key (str): user key to pastebin (part of the login system).
            api_dev_key (str): dev key to pastebin.

            post_url (str): url to create, delete pastes,
                            get user settings and publications.
            raw_private (str): url to read user's private pastes.
            raw_public (str): url to read user's public and unlisted pastes.

        """
        self.api_user_key: Final[str] = os.environ.get("pbin_api_user_key")
        self.api_dev_key: Final[str] = os.environ.get("pbin_api_dev_key")

        self.post_url: Final[str] = os.environ.get("pbin_post_url")
        self.raw_private: Final[str] = os.environ.get("pbin_private_raw_url")
        self.raw_public: Final[str] = os.environ.get("pbin_public_raw_url")

    def __str__(self):
        return "Pastebin User"


class Github_user:
    """Github User."""

    def __init__(self):
        self.token = os.environ.get("hub_token")
        self.api_gist_url = os.environ.get("hub_gist_url")
        self.api_repo_url = os.environ.get("hub_repo_url")
        self.username = os.environ.get("hub_username")

    def __str__(self):
        return "Github User"


class Animal_user:
    def __init__(self):
        """Config params.

        Args:
            url_catapi (str): url to catapi.
            url_randfox (str): url yo randfox.
            url_shibe (str): url to shibe.

        """
        self.url_catapi = os.environ.get("catapi_url")
        self.url_shibe = os.environ.get("shibe_url")
        self.url_randfox = os.environ.get("random_fox_url")

    def __str__(self):
        return "Animal user"


class Relink_user:
    """Relink config urls."""

    url_relink = os.environ.get("url_relink")
    url_clean = os.environ.get("url_clean")

    def __str__(self):
        return "Relink user"
