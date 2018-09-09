import logging

import aiohttp

from .github import GitHub


log = logging.getLogger(__name__)


async def find_clog(url: str, *, session=aiohttp.ClientSession) -> str:
    for host in {GitHub}:
        if host.matches(url):
            return await host.find_clog(url, session=session)

    log.warning(f'could not find changelog given url {url}')


__all__ = ['find_clog']
