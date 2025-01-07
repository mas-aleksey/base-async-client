# coding:utf-8
"""
Asynchronous HTTP client

This module provides BaseClient class for building asynchronous HTTP clients,
with methods for making requests, handling responses, and parsing data.
"""
import logging

from async_client._client import BaseClient
from async_client._exceptions import BaseError, ClientError
from async_client._settnigs import ClientConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ %(levelname)-7.7s ]  %(message)s",
    handlers=[logging.StreamHandler()],
)

__all__ = ["BaseClient", "BaseError", "ClientError", "ClientConfig"]
