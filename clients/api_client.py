from typing import Any

from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Base API client. Uses httpx.Client.

        :param client: instance of httpx.Client
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Makes GET-request.
        
        :param url: endpoint URL.
        :param params: request query parameters (e.g. ?key=value).
        :return: httpx.Response object.
        """
        return self.client.get(url, params=params)
    
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Makes POST-request.
        
        :param url: endpoint URL.
        :param json: data in JSON format.
        :param data: Formatted form data (e.g. application/x-www-form-urlencoded).
        :param files: Files to be uploaded to server.
        :return: httpx.Response object.
        """
        return self.client.post(url, json=json, data=data, files=files)
    
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Makes PATCH-request.

        :param url: endpoint URL.
        :param json: data in JSON format.
        :return: Оhttpx.Response object.
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Makes DELETE-request.

        :param url: endpoint URL.
        :return: httpx.Response object.
        """
        return self.client.delete(url)
    

    