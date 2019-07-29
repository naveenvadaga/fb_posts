import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.post_interactor import PostInteractor


class TestGetPositiveReactedPosts(unittest.TestCase):

    def test_get_positive_reacted_posts_returns_post_ids_list(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        posts_id = [1, 2, 3, 4]
        mock_response = {"posts": posts_id}
        mock_storage.get_more_positive_reacted_post_ids.return_value = posts_id
        mock_json_presenter.get_more_positive_reacted_posts_response.return_value = mock_response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_post_metrics = post_interactor.\
            get_more_positive_reacted_post_ids()

        mock_storage.get_more_positive_reacted_post_ids.assert_called_once()
        mock_json_presenter.get_more_positive_reacted_posts_response.\
            assert_called_once_with(
            posts_id)
        assert response_from_get_post_metrics == mock_response
