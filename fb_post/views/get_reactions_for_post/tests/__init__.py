# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_reactions_for_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01GetReactionsForPostAPITestCase

__all__ = [
    "TestCase01GetReactionsForPostAPITestCase"
]
