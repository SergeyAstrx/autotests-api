from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    userId: str


class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Method fetches list of courses.

        :param query: Dict containing userId.
        :return: Endpoint response (httpx.Response).
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Method fetches course.

        :param course_id: Course id.
        :return: Endpoint response (httpx.Response).
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Method creates course.

        :param request: Dict containing title, maxScore, minScore, description, estimatedTime, 
        previewFileId, createdByUserId.
        :return: Endpoint response (httpx.Response).
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Method updates course.

        :param course_id: Course id.
        :param request: Dict containing title, maxScore, minScore, description, estimatedTime.
        :return: Endpoint response (httpx.Response).
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method deletes course.

        :param course_id: Course id.
        :return: Endpoint response (httpx.Response).
        """
        return self.delete(f"/api/v1/courses/{course_id}")
