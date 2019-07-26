import unittest
from fb.presenters.json_presenter import *
from django_swagger_utils.drf_server.exceptions import BadRequest


class TestRaiseInvalidPostId(unittest.TestCase):

    def test_raise_invalid_post_id_raise_exception(self):
        json_presenter = Presenter()
        with self.assertRaises(BadRequest):
            json_presenter.raise_invalid_post_id()
