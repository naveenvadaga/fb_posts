# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "get_user_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "person/{user_id}/post/"

from .test_case_01 import TestCase01GetUserPostsAPITestCase

__all__ = [
    "TestCase01GetUserPostsAPITestCase"
]
