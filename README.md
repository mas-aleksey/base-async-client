# Async Client Library

[![publish](https://github.com/mas-aleksey/async-client/workflows/Build/badge.svg)](https://github.com/mas-aleksey/async-client/actions?query=workflow%3A%22build%22)
[![coverage](https://coveralls.io/repos/mas-aleksey/async-client/badge.svg)](https://coveralls.io/r/mas-aleksey/async-client?branch=python-3)
[![codeql](https://github.com/mas-aleksey/async-client/workflows/CodeQL/badge.svg)](https://github.com/mas-aleksey/async-client/actions/workflows/codeql-analysis.yml)
[![pypi](https://img.shields.io/pypi/v/async-client-lib.svg)](https://pypi.python.org/pypi/async-client-lib)
[![license](https://img.shields.io/github/license/mas-aleksey/async-client)](https://github.com/mas-aleksey/async-client/blob/main/LICENSE)

## 🚀 Project Overview
`async-client-lib` is a sophisticated Python asynchronous HTTP client library designed to provide efficient, flexible, and robust HTTP request handling. Leveraging modern Python packaging tools and best practices, this library offers a comprehensive solution for building resilient network communication interfaces.
## 🛠 Technology Stack
### Core Technologies
- **Language**: Python 3.9+
- **Async Framework**: `aiohttp`
- **Configuration Management**: `pydantic`
- **Retry Mechanism**: `backoff`
### Development Tools
- **Package Management**: Poetry
- **Testing**: pytest, pytest-asyncio
- **Code Quality**: 
  - Formatting: Black
  - Linting: Ruff
  - Type Checking: mypy
## 📂 Project Structure
```
async-client-main/
├── async_client/
│   ├── __init__.py       # Core library initialization
│   ├── _client.py        # Base async HTTP client implementation
│   └── _exceptions.py    # Custom exception handling
├── pyproject.toml        # Project configuration and dependencies
├── README.md             # Project documentation
└── LICENSE               # MIT License
```
## 🔧 Key Components
### 1. BaseClient
- Provides core async HTTP request management
- Supports type-safe response parsing
- Configurable client settings
### 2. ClientConfig
- Manages client configuration parameters
- Supports SSL verification, timeouts, and host configuration
### 3. Error Handling
- Custom exception classes (`BaseError`, `ClientError`)
- Comprehensive error logging and reporting
## 🚀 Quick Start
### Installation
```bash
pip install async-client-lib
# Or using Poetry
poetry add async-client-lib
```
### Usage Example
```python

from typing import List, Dict
from pydantic import BaseModel

from async_client import BaseClient, ClientConfig


class SlideShow(BaseModel):
    title: str
    author: str
    date: str
    slides: List[Dict]


class SlideShowResponse(BaseModel):
    slideshow: SlideShow


class HttpBinClient(BaseClient):

    async def get_json(self) -> SlideShow:
        url = self.get_path("json")
        resp = await self._perform_request("GET", url)
        data = self.load_schema(resp.body, SlideShowResponse)
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
## 🛡 Development
### Setup
```bash
# Install dependencies
poetry install
# Run tests
poetry run pytest
# Code quality checks
poetry run black .
poetry run ruff check .
```
## 📋 Configuration Options
| Parameter      | Description                     | Default   |
|---------------|--------------------------------|-----------|
| `HOST`        | Base URL for requests          | Required  |
| `SSL_VERIFY`  | SSL certificate verification   | `True`    |
| `CLIENT_TIMEOUT` | Request timeout duration     | `30`      |
## 📄 License
MIT License
## 📞 Contact
Aleksey Matyunin
- Email: matyunin.as@mail.ru
## 🔖 Version
Current version: 0.1.8
---
**Note**: Always refer to the latest documentation and release notes for the most up-to-date information.