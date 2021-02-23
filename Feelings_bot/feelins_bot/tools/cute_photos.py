import aiohttp

from user_classes import Animal_user


async def get_url(url: str):
    """Get url to photo pattern.

    Args:
        url (str): url to get requests

    Returns:
        Coroutine: response.json()

    """
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
    return await response.json()


class Random_animal(Animal_user):
    """Random animal -hruk."""

    def __init__(self):
        super().__init__()

    def __str__(self):
        """Read name."""
        return "Random animal -hruk"

    async def get_catapi_url(self) -> str:
        """Get cat photo url.

        Returns:
            str: url to photo.

        """
        return (await get_url(self.url_catapi))[0]["url"]

    async def get_randfox_url(self) -> str:
        """Get fox photo url.

        Returns:
            str: url to photo.

        """
        return (await get_url(self.url_randfox))["image"]

    async def get_shibe_url(self) -> str:
        """Get random pictures of Shibu Inu, cats or birds.

        Returns:
            str: url to photo.

        """
        return (await get_url(self.url_shibe))[0]
