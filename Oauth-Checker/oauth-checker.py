"""
HFC.CRM.Service Oauth Checker Script.

Note: MUST HAVE HFC.CRM.Service RUNNING IN DEBUGGER.
This script will hit the 'token' endpoint to get a Bearer token.
It will then uses the token to make a couple requests against the api.
"""

from datetime import datetime

import requests

from src.config import ConfigManager
from src.helpers import exit_now, get_debug_url
from src.requests_fn import get_request, post_request

__tokenKey__ = "access_token"
__tokenStrKey__ = "token_str"
__urlKey__ = "api_url"
__expkey__ = "expires"
__pathKey__ = "service_csproj_key"
# __qaApiKey = "qa_api_url"


def get_token_from_api(oauth_url: str, user_model: dict):
    """Goes to url with user data to retrieve Auth Token.

    Arguments:
        oauth_url {str} -- [description]
        user_model {dict} -- [description]

    Returns:
        dict {token, type, issued, expires, scope} -- values are all strings
    """
    res = post_request(url=oauth_url, data=user_model)
    print(f"Status Code from Auth Endpoint: {res.status_code}")

    if res.status_code is not 200:
        exit_now()

    data = res.json()
    return {
        __tokenStrKey__: data["access_token"],
        "type": str(data["token_type"]).capitalize(),
        "issued": data["issued"],
        __expkey__: data["expires"],
        "scope": data["scope"]
    }


def get_token(config: ConfigManager, api_url: str):
    """Get Token from either api or config manager."""
    token_endpoint = api_url + "token"

    if __tokenKey__ not in config:
        print(
            "No Token stored in app data."
            f"\nCalling {token_endpoint} for bearer token"
        )
        token = get_token_from_api(token_endpoint, config["user"])
        config[__tokenKey__] = token
        return token
    else:
        token = config[__tokenKey__]

    # check if token has expired
    token_exp_str = token[__expkey__].split('.')[0]
    if datetime.strptime(token_exp_str, '%Y-%m-%dT%H:%M:%S') < datetime.now():
        print("Getting new token because stored token expired")
        token = get_token_from_api(token_endpoint, config["user"])
        config[__tokenKey__] = token
    else:
        print("Using token stored in app.data.json")

    return token


def main():
    """Run main function of script."""
    print()  # just to start console on new
    try:
        config = ConfigManager()
    except FileNotFoundError:
        print(f"file {config.__datafile__} is missing")
        exit()

    if __urlKey__ not in config:
        print(
            f"Please enter the url for the api in app.data.json with key "
            "'{__urlKey__}'."
        )
        exit_now()

    api_url = config[__urlKey__]

    # checking if url is correct
    print(f"Checking if api at {api_url} is up ...")
    check_api = get_request(api_url)
    if check_api.status_code is not 200:
        print(f"Could not reach {check_api}...")
        print("Either the url is wrong, or the api is not up.")
        print("Please change the url in app.data.json file or debug the api.")
        exit_now()
    else:
        print(f"API url {api_url} is working!\n")

    # Get Auth Token and Create Auth Header
    token = get_token(config, api_url)
    auth_header = {"Authorization": f"Bearer {token[__tokenStrKey__]}"}
    print(f"\nGenerated Auth Header: {auth_header}")

    # Hit GetUserInfo endpoint
    user_endpoint = api_url + 'api/GetUserInfo'
    print(f"\n\nCalling {user_endpoint} with Auth Header...\n")

    # calling api here
    res = get_request(url=user_endpoint, headers=auth_header)
    print(f"Status from GetUserInfo Endpoint: {res.status_code}")
    print(f"Headers from Response: {res.headers}")
    print(f"\nContent from GetUserInfo API: {res.json()}")

# end of main #


if __name__ == '__main__':
    main()
