import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage, GetPostDto
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class TestGetPostDetails(unittest.TestCase):

    def test_get_post_details_returns_post_details(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)

        post_id = 1
        mock_get_post_dto = Mock(spec=[field.name for field in fields(GetPostDto)])
        response = {"post_id": 1}

        mock_storage.get_post_details.return_value = mock_get_post_dto
        mock_json_presenter.get_post_details_response.return_value = response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_post_metrics = post_interactor.get_post_details(post_id)

        mock_storage.get_post_details.assert_called_once_with(post_id)
        mock_json_presenter.get_post_details_response.assert_called_once_with(mock_get_post_dto)
        assert response_from_get_post_metrics == response
