import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor


class TestGetPostReactedByUser(unittest.TestCase):

    def test_get_post_reacted_by_user_interactor_returns_post_ids(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        user_id = 1
        post_id_list = [1, 2, 3, 4]
        mock_response = {'posts': post_id_list}
        mock_storage.get_post_reacted_by_user.return_value = post_id_list
        mock_json_presenter.get_post_reacted_by_user_response.return_value = mock_response
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_post_count_method = post_interactor.get_post_reacted_by_user_interactor(
            user_id)
        mock_storage.get_post_reacted_by_user.assert_called_once_with(user_id)
        mock_json_presenter.get_post_reacted_by_user_response.assert_called_once_with(
            post_id_list)
        assert response_from_get_post_count_method == mock_response
