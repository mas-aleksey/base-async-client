Asynchronous HTTP client
=======

.. image:: https://travis-ci.org/mas-aleksey/async-client.svg
    :target: https://travis-ci.org/mas-aleksey/async-client
.. image:: https://coveralls.io/repos/mas-aleksey/async-client/badge.svg
    :target: https://coveralls.io/r/mas-aleksey/async-client?branch=python-3
.. image:: https://github.com/mas-aleksey/async-client/workflows/CodeQL/badge.svg
    :target: https://github.com/mas-aleksey/async-client/actions/workflows/codeql-analysis.yml
.. image:: https://img.shields.io/pypi/v/async-client-lib.svg
    :target: https://pypi.python.org/pypi/async-client-lib
.. image:: https://img.shields.io/github/license/mas-aleksey/async-client
    :target: https://github.com/mas-aleksey/async-client/blob/main/LICENSE


This module provides BaseClient class for building asynchronous HTTP clients,
with methods for making requests, handling responses, and parsing data.

Examples
========

.. code-block:: python
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
