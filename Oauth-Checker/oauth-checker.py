"""
HFC.CRM.Service Oauth Checker Script.

Note: MUST HAVE HFC.CRM.Service RUNNING IN DEBUGGER.
This script will hit the 'token' endpoint to get a Bearer token.
It will then uses the token to make a couple requests against the api.
"""
from src.main import main

if __name__ == "__main__":
    main()
