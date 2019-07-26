# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "get_post_reactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01GetPostReactionsAPITestCase

__all__ = [
    "TestCase01GetPostReactionsAPITestCase"
]
