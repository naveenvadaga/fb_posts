# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "get_post_reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/react/count/"

from .test_case_01 import TestCase01GetPostReactionsCountAPITestCase

__all__ = [
    "TestCase01GetPostReactionsCountAPITestCase"
]
