import logging

from base_client._client import BaseClient
from base_client._exceptions import BaseError, ClientError
from base_client._settnigs import ClientConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ %(levelname)-7.7s ]  %(message)s",
    handlers=[logging.StreamHandler()],
)

__all__ = ["BaseClient", "BaseError", "ClientError", "ClientConfig"]
