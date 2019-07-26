# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "post_comment_for_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/reply/"

from .test_case_01 import TestCase01PostCommentForCommentAPITestCase

__all__ = [
    "TestCase01PostCommentForCommentAPITestCase"
]
