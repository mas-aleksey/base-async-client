from os import getenv

from pydantic_settings import BaseSettings

MAX_RETRY = int(getenv("MAX_RETRY", "3"))


class ClientConfig(BaseSettings):
    HOST: str
    SSL_VERIFY: bool = True
    CLIENT_TIMEOUT: int = 30
