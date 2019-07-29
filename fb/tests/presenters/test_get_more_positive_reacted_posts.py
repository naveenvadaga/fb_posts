import unittest
from fb.presenters.json_presenter import *


class TestGetPositiveReactedPosts(unittest.TestCase):

    def test_positive_reacted_posts(self):
        post_id_list = [1, 2, 3, 4]

        json_presenter = JsonPresenter()
        response = json_presenter.get_more_positive_reacted_posts_response(post_id_list)

        response_id_list = response['posts']

        assert response_id_list[0]['id'] in post_id_list
