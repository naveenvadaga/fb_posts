import unittest
from fb.presenters.json_presenter import *


class TestCreatePost(unittest.TestCase):

    def test_create_post_response(self):
        post_id = 1

        json_presenter = JsonPresenter()
        response = json_presenter.create_post_response(post_id)

        assert response['id'] == post_id



