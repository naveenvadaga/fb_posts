# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_post_reacted_by_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "person/{user_id}/post/react/"

from .test_case_01 import TestCase01GetPostReactedByUserAPITestCase

__all__ = [
    "TestCase01GetPostReactedByUserAPITestCase"
]
