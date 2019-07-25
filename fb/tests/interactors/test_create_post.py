import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor


class TestCreatePost(unittest.TestCase):

    def test_create_post_returns_post_id(self):
        mock_storage = Mock(spec=Storage)
        mock_storage.create_post.return_value = 1
        mock_json_presenter = Mock(spec=JsonPresenter)
        mock_json_presenter.create_post_response.return_value = {'id': 1}

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_create_post_method = post_interactor.create_post_interactor(1,
                                                                                  "first post")

        mock_storage.create_post.assert_called_once_with(1, 'first post')
        mock_json_presenter.create_post_response.assert_called_once_with(1)
        assert response_from_create_post_method == {'id': 1}
