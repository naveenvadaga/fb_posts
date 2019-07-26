# pylint: disable=wrong-import-position

APP_NAME = "fb"
OPERATION_NAME = "get_post_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/metrics/"

from .test_case_01 import TestCase01GetPostMetricsAPITestCase

__all__ = [
    "TestCase01GetPostMetricsAPITestCase"
]
