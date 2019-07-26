# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "post_react_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01PostReactToPostAPITestCase

__all__ = [
    "TestCase01PostReactToPostAPITestCase"
]
