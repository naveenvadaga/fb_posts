# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "add_post_reaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01AddPostReactionAPITestCase

__all__ = [
    "TestCase01AddPostReactionAPITestCase"
]
