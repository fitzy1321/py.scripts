"""Modules Containing Requests Functions."""

import requests
from src.helpers import exit_now


def get_request(url: str, headers=None, data=None):
    """Make get request."""
    headers = "" if headers is None else headers
    try:
        if data is None:
            res = requests.get(url=url, headers=headers)
        else:
            res = requests.get(url=url, data=data, headers=headers)

        return res
    except (
        requests.exceptions.HTTPError,
        ConnectionRefusedError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ConnectionError
    ):
        print("A Problem occured trying to hit api")
        print("Please check url in app.data.json is correct or")
        print("make sure service api is running...")
        exit_now()


def post_request(url: str, data=None, headers=None):
    """Make post request."""
    headers = "" if headers is None else headers
    try:
        if data is None:
            res = requests.post(url=url, headers=headers)
        else:
            res = requests.post(url=url, data=data, headers=headers)

        return res
    except (
        requests.exceptions.HTTPError,
        ConnectionRefusedError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ConnectionError
    ):
        print("A Problem occured trying to hit api")
        print("Please check url in app.data.json is correct or")
        print("make sure service api is running...")
        exit_now()
