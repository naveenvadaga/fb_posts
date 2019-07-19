# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_comment_for_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/reply/"

from .test_case_01 import TestCase01PostCommentForCommentAPITestCase
from .test_case_02 import TestCase02PostCommentForCommentAPITestCase

__all__ = [
    "TestCase01PostCommentForCommentAPITestCase",
    "TestCase02PostCommentForCommentAPITestCase"
]
