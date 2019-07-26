# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "add_comment_reply"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/reply/"

from .test_case_01 import TestCase01AddCommentReplyAPITestCase

__all__ = [
    "TestCase01AddCommentReplyAPITestCase"
]
