import pytest
from _exceptions import BaseError, ClientError
from aioresponses import aioresponses


async def test_get_data_200(client):
    with aioresponses() as m:
        m.get("http://127.0.0.1:8010/data", status=200, payload={"some": "some", "data": "data"})
        data = await client.get_data()

    m.assert_called_with(url="http://127.0.0.1:8010/data", method="GET", ssl=True)
    assert data.some == "some"
    assert data.data == "data"


@pytest.mark.parametrize(
    "body,expected_error",
    [
        (
            b'{"foo": "bar"}',
            "ValidationError in 'TestSchema': 'some' - Field required, 'data' - Field required. input: b'{\"foo\": \"bar\"}'",  # noqa: E501
        ),
        (
            b"foo-bar",
            "ValidationError in 'TestSchema': '__root__' - Expecting value: line 1 column 1 (char 0). input: b'foo-bar'",  # noqa: E501
        ),
    ],
)
async def test_get_data_validate_error(client, body, expected_error):
    with aioresponses() as m, pytest.raises(BaseError) as exc:
        m.get("http://127.0.0.1:8010/data", status=200, body=body)
        await client.get_data()
    assert str(exc.value) == expected_error


async def test_get_data_timeout_error(client):
    with aioresponses() as m, pytest.raises(ClientError) as exc:
        m.get("http://127.0.0.1:8010/data", timeout=True, repeat=True)
        await client.get_data()
    assert "TimeoutError" in str(exc.value)


async def test_get_data_400(client):
    with aioresponses() as m, pytest.raises(BaseError) as exc:
        m.get("http://127.0.0.1:8010/data", status=400, payload={"error": "something went wrong"})
        await client.get_data()
    assert "something went wrong" in str(exc.value)


async def test_get_data_500(client):
    with aioresponses() as m, pytest.raises(ClientError) as exc:
        m.get(
            "http://127.0.0.1:8010/data", status=500, payload={"error": "server error"}, repeat=True
        )
        await client.get_data()
    assert "server error" in str(exc.value)
