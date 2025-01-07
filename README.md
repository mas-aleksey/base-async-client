Asynchronous HTTP client
=======

[![build](https://github.com/mas-aleksey/async-client/workflows/Publish/badge.svg)](https://github.com/mas-aleksey/async-client/actions?query=workflow%3A%22publish%22)
[![coverage](https://coveralls.io/repos/mas-aleksey/async-client/badge.svg)](https://coveralls.io/r/mas-aleksey/async-client?branch=python-3)
[![codeql](https://github.com/mas-aleksey/async-client/workflows/CodeQL/badge.svg)](https://github.com/mas-aleksey/async-client/actions/workflows/codeql-analysis.yml)
[![pypi](https://img.shields.io/pypi/v/async-client-lib.svg)](https://pypi.python.org/pypi/async-client-lib)
[![license](https://img.shields.io/github/license/mas-aleksey/async-client)](https://github.com/mas-aleksey/async-client/blob/main/LICENSE)

This module provides BaseClient class for building asynchronous HTTP clients,
with methods for making requests, handling responses, and parsing data.

Examples
========

```python

from pydantic import BaseModel
from async_client import BaseClient, ClientConfig


class TestSchema(BaseModel):
    some: str
    data: str


class TestClient(BaseClient):

    async def get_data(self) -> TestSchema:
        url = self.get_path("data")
        resp = await self._perform_request("GET", url)
        data = self.load_schema(resp.body, TestSchema)
        return data


async def main():
    config = ClientConfig(HOST="http://127.0.0.1:8010", CLIENT_TIMEOUT=1)
    async with TestClient(config) as client:
        result = await client.get_data()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```