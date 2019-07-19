# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_reactions_count_for_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/react/count/"

from .test_case_01 import TestCase01GetReactionsCountForPostsAPITestCase

__all__ = [
    "TestCase01GetReactionsCountForPostsAPITestCase"
]
