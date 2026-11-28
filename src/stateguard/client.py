
"""HTTP client for authenticated communication with Stockroom."""

import http.cookiejar
import json
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import (
    HTTPCookieProcessor,
    Request,
    build_opener,
)


class CSRFTokenParser(HTMLParser):
    """Extract the CSRF token from Stockroom's login form."""

    def __init__(self):
        super().__init__()
        self.token = None

    def handle_starttag(self, tag, attrs):
        if tag != "input":
            return

        attributes = dict(attrs)

        if attributes.get("name") == "csrf_token":
            self.token = attributes.get("value")


class StockroomClient:
    """Send HTTP requests to Stockroom while preserving authentication."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.csrf_token = None

        self.cookies = http.cookiejar.CookieJar()
        self.opener = build_opener(
            HTTPCookieProcessor(self.cookies)
        )

    def _request(self, method, path, data=None, headers=None):
        """Send an HTTP request and return its status and response body."""

        url = self.base_url + "/" + path.lstrip("/")

        request = Request(
            url,
            data=data,
            headers=headers or {},
            method=method.upper(),
        )

        try:
            with self.opener.open(request, timeout=5) as response:
                return response.status, response.read().decode("utf-8")

        except HTTPError as error:
            return error.code, error.read().decode("utf-8")

        except URLError as error:
            return None, str(error.reason)

    def login(self, username: str, password: str) -> bool:
        """Log in through Stockroom's web form and retain the session."""

        status, page = self._request("GET", "/login")

        if status != 200:
            return False

        parser = CSRFTokenParser()
        parser.feed(page)

        if not parser.token:
            return False

        self.csrf_token = parser.token

        form_data = urlencode({
            "csrf_token": self.csrf_token,
            "username": username,
            "password": password,
            "remember": "y",
            "submit": "Sign In",
        }).encode("utf-8")

        status, _ = self._request(
            "POST",
            "/login",
            data=form_data,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": self.base_url + "/login",
            },
        )

        return status == 200

    def get(self, path: str):
        """Send an authenticated GET request."""

        return self._request("GET", path)

    def post(self, path: str, json_body: dict):
        """Send an authenticated JSON POST request."""

        data = json.dumps(json_body).encode("utf-8")

        return self._request(
            "POST",
            path,
            data=data,
            headers={
                "Content-Type": "application/json",
                "X-CSRFToken": self.csrf_token or "",
            },
        )
