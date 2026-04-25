from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Client for endpoint /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Method creates user.

        :param request: typed dict.
        :return: endpoint response (httpx.Response)
        """
        return self.post("/api/v1/users", json=request)