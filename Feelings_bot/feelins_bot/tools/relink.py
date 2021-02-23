import aiohttp

from user_classes import Relink_user


class Relink(Relink_user):
    """Class for url shorteners."""

    def __str__(self):
        return "Relink class"

    @staticmethod
    async def create_relink(url: str) -> str:
        """Create new link on https://rel.ink/ .

        Args:
            url (str): url to shorten.

        Returns:
            str: shortened url.

        """
        async with aiohttp.ClientSession() as session:
            respon = await session.post(Relink.url_relink, data={"url": url})
        return 'https://rel.ink/' + (await respon.json())['hashid']

    @staticmethod
    async def read_relink(url: str) -> str:
        """Read short link on https://rel.ink/ .

        Args:
            url (str): short url.

        Returns:
            str: usual url.

        """
        async with aiohttp.ClientSession() as session:
            response = await session.get(Relink.url_relink + url[-6:] + "/")
        return (await response.json())['url']

    @staticmethod
    async def create_clean(url: str) -> str:
        """Create new link on cleanuri.com .

        Args:
            url (str): url to shorten.

        Returns:
            str: shortened url.

        """
        async with aiohttp.ClientSession() as session:
            response = await session.post(Relink.url_clean, data={"url": url})
        return (await response.json())["result_url"]
