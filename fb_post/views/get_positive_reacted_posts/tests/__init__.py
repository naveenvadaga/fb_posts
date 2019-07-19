# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_positive_reacted_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/react/positive/"

from .test_case_01 import TestCase01GetPositiveReactedPostsAPITestCase

__all__ = [
    "TestCase01GetPositiveReactedPostsAPITestCase"
]
