import unittest
from fb.presenters.json_presenter import *


class TestCreateComment(unittest.TestCase):

    def test_create_comment_response(self):
        comment_id = 1
        json_presenter = JsonPresenter()
        response = json_presenter.create_comment_response(comment_id)

        assert response['id'] == comment_id
