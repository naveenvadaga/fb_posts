# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_react_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/react/"

from .test_case_01 import TestCase01PostReactToCommentAPITestCase

__all__ = [
    "TestCase01PostReactToCommentAPITestCase"
]
