Asynchronous HTTP client
=======

[![publish](https://github.com/mas-aleksey/async-client/workflows/Build/badge.svg)](https://github.com/mas-aleksey/async-client/actions?query=workflow%3A%22build%22)
[![coverage](https://coveralls.io/repos/mas-aleksey/async-client/badge.svg)](https://coveralls.io/r/mas-aleksey/async-client?branch=python-3)
[![codeql](https://github.com/mas-aleksey/async-client/workflows/CodeQL/badge.svg)](https://github.com/mas-aleksey/async-client/actions/workflows/codeql-analysis.yml)
[![pypi](https://img.shields.io/pypi/v/async-client-lib.svg)](https://pypi.python.org/pypi/async-client-lib)
[![license](https://img.shields.io/github/license/mas-aleksey/async-client)](https://github.com/mas-aleksey/async-client/blob/main/LICENSE)

This module provides BaseClient class for building asynchronous HTTP clients,
with methods for making requests, handling responses, and parsing data.

Example
========

```python

from typing import List, Dict
from pydantic import BaseModel

from async_client import BaseClient, ClientConfig


class Slideshow(BaseModel):
    title: str
    author: str
    date: str
    slides: List[Dict]


class SlideshowResponse(BaseModel):
    slideshow: Slideshow


class HttpBinClient(BaseClient):

    async def get_json(self) -> Slideshow:
        url = self.get_path("json")
        resp = await self._perform_request("GET", url)
        data = self.load_schema(resp.body, SlideshowResponse)
        return data.slideshow


async def main():
    config = ClientConfig(
        HOST="https://httpbin.org",
        SSL_VERIFY=True,
        CLIENT_TIMEOUT=30,
    )
    async with HttpBinClient(config) as client:
        slideshow = await client.get_json()
        print(slideshow)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```