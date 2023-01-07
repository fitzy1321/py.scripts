from unittest.mock import MagicMock

import aiohttp  # pip install aiohttp
import pytest  # pip install pytest pytest-asyncio
from asyncmock import AsyncMock  # pip install asyncmock

# pytest -rP test_aiohttp_mock.py


@pytest.fixture
def aiomock() -> tuple:
    session = AsyncMock()
    response = AsyncMock()
    response.json.return_value = {"body": "asdf"}
    response.raise_for_status = MagicMock(side_effect=aiohttp.ClientError)
    session.request = MagicMock(return_value=response)
    return session, response


@pytest.mark.asyncio
async def test_async_mock_works(aiomock):
    session, response = aiomock
    with pytest.raises(aiohttp.ClientError):
        async with session:
            async with session.request(
                method="GET", url="https://catfact.ninja/fact"
            ) as _resp:
                _resp.raise_for_status()
                result = await _resp.json()

    session.request.assert_called_once()
    response.raise_for_status.assert_called_once()
    response.json.assert_not_called()