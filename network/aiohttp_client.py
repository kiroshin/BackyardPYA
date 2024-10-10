#  aiohttp_client.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2024.

import aiohttp


# 기본값 100 커넥션이다. 이 정도면 차고 넘친다.
# 런루프 종료 시에는 반드시 닫아줘야 한다.
# https://docs.aiohttp.org/en/stable/client_advanced.html
class AioHttpClient:
    SESSION: aiohttp.ClientSession | None = None

    @staticmethod
    def __bootup__():
        if not AioHttpClient.SESSION or AioHttpClient.SESSION.closed:
            AioHttpClient.SESSION = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))

    @staticmethod
    async def __shutdown__():
        if AioHttpClient.SESSION and not AioHttpClient.SESSION.closed:
            await AioHttpClient.SESSION.close()
