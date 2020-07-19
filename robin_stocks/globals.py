"""Holds the session header and other global variables."""
from requests import Session
import copy


# Keeps track on if the user is logged in or not.
LOGGED_IN = False
# The session object for making get and post requests.
SESSION = Session()
SESSION.headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=1",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "X-Robinhood-API-Version": "1.315.0",
    "Connection": "keep-alive",
    "User-Agent": "*"
}

SESSION_ORIGINAL = Session()
SESSION_ORIGINAL.headers = copy.copy(SESSION.headers)
