# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_comment_replies"
REQUEST_METHOD = "get"
URL_SUFFIX = "comment/{comment_id}/replies/"

from .test_case_01 import TestCase01GetCommentRepliesAPITestCase
from .test_case_02 import TestCase02GetCommentRepliesAPITestCase
__all__ = [
    "TestCase01GetCommentRepliesAPITestCase",
    "TestCase02GetCommentRepliesAPITestCase"
]
