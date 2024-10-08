#  test_http_aio_randomuser_access.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

from unittest import IsolatedAsyncioTestCase
from http_aio_client import HttpAioClient
from http_aio_randomuser_access import HttpAioRandomuserAccess


class TestHttpAioRandomuserAccess(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        HttpAioClient.__bootup__()
        self.access = HttpAioRandomuserAccess()

    async def asyncTearDown(self):
        await HttpAioClient.__shutdown__()

    async def test_get_all_user(self):
        users = await self.access.get_all_user(100)
        print(users)
        self.assertTrue(len(users) == 100)

