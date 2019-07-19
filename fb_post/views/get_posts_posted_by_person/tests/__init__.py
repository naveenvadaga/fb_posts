# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_posts_posted_by_person"
REQUEST_METHOD = "get"
URL_SUFFIX = "person/{user_id}/post/"

from .test_case_01 import TestCase01GetPostsPostedByPersonAPITestCase

__all__ = [
    "TestCase01GetPostsPostedByPersonAPITestCase"
]
