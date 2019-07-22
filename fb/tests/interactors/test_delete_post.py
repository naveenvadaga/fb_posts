import unittest
from unittest.mock import Mock

from django.core.exceptions import ObjectDoesNotExist
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor


class DeletePostTest(unittest.TestCase):

    def test_delete_post_returns_200_status(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)

        response_send = {'status': 'successfully deleted'}
        mock_storage.delete_post.return_value = None
        mock_json_presenter.delete_post_response.return_value = response_send
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_delete_post_method = post_interactor.delete_post_interactor(1)

        mock_storage.delete_post.assert_called_once_with(1)
        mock_json_presenter.delete_post_response.assert_called_once_with()
        assert response_from_delete_post_method == response_send

    def test_delete_post_returns_bad_requests(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)

        mock_storage.delete_post.side_effect = ObjectDoesNotExist
        mock_json_presenter.bad_request_invalid_post_id.side_effect = BadRequest
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        with self.assertRaises(BadRequest):
            post_interactor.delete_post_interactor(1)

        mock_storage.delete_post.assert_called_once_with(1)
        mock_json_presenter.bad_request_invalid_post_id.assert_called_once_with()