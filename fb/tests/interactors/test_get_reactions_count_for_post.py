import unittest
from unittest.mock import Mock
from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.post_interactor import PostInteractor


class TestGetReactionsCountForPost(unittest.TestCase):

    def test_get_reactions_count_for_all_posts_returns_count(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)

        count = 3
        mock_response = {'count': count}

        mock_storage.get_total_post_reactions_count.return_value = count
        mock_json_presenter.get_post_reactions_count_response.return_value = mock_response
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_reactions_count_post = post_interactor. \
            get_post_reactions_count()

        mock_storage.get_total_post_reactions_count.assert_called_once()
        mock_json_presenter.get_post_reactions_count_response. \
            assert_called_once_with(count)
        assert response_from_get_reactions_count_post == mock_response
