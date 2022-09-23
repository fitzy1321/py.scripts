from __future__ import annotations

import asyncio
import logging
from pprint import pprint
from typing import Any, Awaitable, Callable, Optional, Type, TypeVar, Union

import aiohttp  # pip install --upgrade aiohttp


log = logging.getLogger(__name__)

BACKOFF = 2
TRIES = 5

RT = TypeVar("RT")  # Return type of the wrapped function


class NoRetry(Exception):
    """
    Exception to prevent further tries

    :param exc: optional exception to re-raise instead of NoRetry if provided,
        allowing a "pass-through" for the original exception
    """

    def __init__(self, *args, exc: Optional[Exception] = None):
        self.exc = exc


# An example of an async decorator, with parameters
# i.e. @retry_async(aiohttp.ClientError, tries=TRIES, backoff=BACKOFF)
def retry_async(
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]],
    tries: int = 4,
    delay: float = 3,
    backoff: int = 2,
) -> Callable[[Callable[..., Awaitable[RT]]], Callable[..., Awaitable[RT]]]:
    """
    Retry decorator to easily retry operations on a per-function level.

    :param exceptions: Exception or tuple of exceptions to handle with retry
    :param tries: Number of times to retry the function
    :param delay: Delay between retries, in seconds
    :param backoff: Exponential backoff between sequential retries
    :return: Result of the wrapped function
    """

    def decorator(func: Callable[..., Awaitable[RT]]) -> Callable[..., Awaitable[RT]]:
        async def wrapper(*args: Any, **kwargs: Any) -> RT:  # type: ignore
            for i in range(tries):
                try:
                    return await func(*args, **kwargs)
                except NoRetry as e:
                    raise e.exc or e
                except exceptions as e:
                    if i >= tries - 1:  # last try
                        raise e
                    import traceback

                    log.warning(
                        f"Exception {e} while calling '{func.__name__}'. "
                        f"Retrying in {delay} sec."
                    )
                    log.warning(f"Unexpected exception: {traceback.format_exc()}")
                    await asyncio.sleep(delay * backoff**i)  # exponential backoff

        return wrapper

    return decorator


@retry_async(aiohttp.ClientError, tries=TRIES, backoff=BACKOFF)
async def call_api_async(
    url: str,
    method: str = "GET",
    params: Optional[dict[Any, Any]] = None,
    no_retry: Optional[set[int]] = None,
) -> dict[str, Any]:
    """
    Make an asynchronous request to a API endpoint.
    """
    try:
        async with aiohttp.request(
            method,
            url,
            params=params,
        ) as resp:
            resp.raise_for_status()
            return await resp.json()
    except aiohttp.ClientResponseError as e:
        if no_retry and e.status is not None and e.status in no_retry:
            raise NoRetry(exc=e) from e
        raise e


async def do_async_things(i):
    await asyncio.sleep(1)
    return await call_api_async(
        f"https://fakestoreapi.com/products/{i}", no_retry={400, 403, 404}
    )


async def main():
    # immediately puts task onto event loop with `asyncio.create_task(...)`
    tasks = [asyncio.create_task(do_async_things(i)) for i in range(1, 20)]

    # wait for all tasks to finish
    results = await asyncio.gather(*tasks)

    # loop over results of multiple async calls
    for r in results:
        pprint(r, indent=2)

    return 0


if __name__ == "__main__":
    # Start event loop with main
    exit_code = asyncio.run(main())
    raise SystemExit(exit_code)
