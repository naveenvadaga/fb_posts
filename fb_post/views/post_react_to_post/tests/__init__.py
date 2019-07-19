# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_react_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01PostReactToPostAPITestCase
from .test_case_02 import TestCase02PostReactToPostAPITestCase
from .test_case_03 import TestCase03PostReactToPostAPITestCase

__all__ = [
    "TestCase01PostReactToPostAPITestCase",
    "TestCase02PostReactToPostAPITestCase",
    "TestCase03PostReactToPostAPITestCase"
]
