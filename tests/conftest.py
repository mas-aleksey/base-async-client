import sys
from logging import config as logger_config

import pytest
import pytest_asyncio
from pydantic import BaseModel

from base_client import BaseClient, ClientConfig


class TestSchema(BaseModel):
    some: str
    data: str


class TestClient(BaseClient):

    async def get_data(self) -> TestSchema:
        url = self.get_path("data")
        resp = await self._perform_request("GET", url)
        data = self.load_schema(resp.body, TestSchema)
        return data


@pytest_asyncio.fixture
async def client():
    config = ClientConfig(HOST="http://127.0.0.1:8010", CLIENT_TIMEOUT=1)
    async with TestClient(config=config) as cli:
        yield cli


@pytest.fixture(autouse=True)
def init_logger() -> None:
    logger_config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "class": "logging.Formatter",
                "format": "%(asctime)s [%(levelname)s] %(name)-5s: %(message)s",
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
                "stream": sys.stdout,
            }
        },
        "loggers": {
            "databases": {"level": "INFO"},
        },
        "root": {
            "level": "DEBUG",
            "formatter": "verbose",
            "handlers": [
                "console",
            ],
        },
    })
