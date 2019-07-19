# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_post_content"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/"

from .test_case_01 import TestCase01PostPostContentAPITestCase

__all__ = [
    "TestCase01PostPostContentAPITestCase"
]
