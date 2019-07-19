# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_react_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/react/"

from .test_case_01 import TestCase01PostReactToCommentAPITestCase
from .test_case_02 import TestCase02PostReactToCommentAPITestCase
from .test_case_03 import TestCase03PostReactToCommentAPITestCase

__all__ = [
    "TestCase01PostReactToCommentAPITestCase",
    "TestCase02PostReactToCommentAPITestCase",
    "TestCase03PostReactToCommentAPITestCase"
]
