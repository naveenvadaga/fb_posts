# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "add_comment_reaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/react/"

from .test_case_01 import TestCase01AddCommentReactionAPITestCase

__all__ = [
    "TestCase01AddCommentReactionAPITestCase"
]
