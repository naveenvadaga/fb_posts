# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "get_user_reacted_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "person/{user_id}/post/react/"

from .test_case_01 import TestCase01GetUserReactedPostAPITestCase

__all__ = [
    "TestCase01GetUserReactedPostAPITestCase"
]
