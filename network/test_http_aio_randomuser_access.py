#  test_http_aio_randomuser_access.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from unittest import IsolatedAsyncioTestCase
from aiohttp_client import AioHttpClient
from aiohttp_randomuser_access import AiohttpRandomuserAccess


class TestHttpAioRandomuserAccess(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        AioHttpClient.__bootup__()
        self.access = AiohttpRandomuserAccess()

    async def asyncTearDown(self):
        await AioHttpClient.__shutdown__()

    async def test_get_all_user(self):
        users = await self.access.get_all_user(100)
        print(users)
        self.assertTrue(len(users) == 100)

