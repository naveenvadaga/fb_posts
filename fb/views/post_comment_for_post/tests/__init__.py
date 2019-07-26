# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "post_comment_for_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/comment/"

from .test_case_01 import TestCase01PostCommentForPostAPITestCase

__all__ = [
    "TestCase01PostCommentForPostAPITestCase"
]
