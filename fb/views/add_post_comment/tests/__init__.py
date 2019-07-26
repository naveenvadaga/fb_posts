# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "add_post_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/comment/"

from .test_case_01 import TestCase01AddPostCommentAPITestCase

__all__ = [
    "TestCase01AddPostCommentAPITestCase"
]
