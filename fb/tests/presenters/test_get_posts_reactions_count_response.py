import unittest
from fb.presenters.json_presenter import *


class TestGetPostsReactionsCountResponse(unittest.TestCase):

    def test_get_posts_reactions_count_response(self):
        count = 10
        json_presenter = JsonPresenter()
        response = json_presenter.get_post_reactions_count_response(count)

        assert response['count'] == count
