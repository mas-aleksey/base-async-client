from typing import Optional


class BaseError(Exception):
    """Base class for all exceptions in application"""

    default_msg = "Unknown error"

    def __init__(self, message: Optional[str] = None, extra: Optional[str] = None) -> None:
        self.message = message or self.default_msg
        if extra:
            self.message = f"{self.message}, info: {extra}"

    def __str__(self) -> str:
        return self.message


class ClientError(BaseError):
    default_msg = "Client error"
