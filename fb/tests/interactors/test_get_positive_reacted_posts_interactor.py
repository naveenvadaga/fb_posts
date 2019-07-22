import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor


class TestGetPositiveReactedPosts(unittest.TestCase):

    def test_get_positive_reacted_posts_interactor_returns_post_ids_list(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        posts_id = [1, 2, 3, 4]
        response = {"posts": posts_id}
        mock_storage.get_positive_reacted_posts.return_value = posts_id
        mock_json_presenter.get_positive_reacted_posts_response.return_value = response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_post_metrics = post_interactor.get_positive_reacted_posts_interactor()

        mock_storage.get_positive_reacted_posts.assert_called_once()
        mock_json_presenter.get_positive_reacted_posts_response.assert_called_once_with(posts_id)
        assert response_from_get_post_metrics == response
