import unittest
from unittest.mock import Mock

from django.core.exceptions import SuspiciousOperation
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb.interactors.storages.storage import Storage, CommentDto
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.comment_interactor import CommentInteractor
from dataclasses import fields


class TestGetCommentReplies(unittest.TestCase):

    def test_get_comment_replies_returns_comment_replies_list(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        reply_one_dto = Mock(spec=[field.name for field in fields(CommentDto)])
        reply_second_dto = Mock(
            spec=[field.name for field in fields(CommentDto)])
        replies_dto_list = [reply_one_dto, reply_second_dto]
        mock_response = [{"comment_id": 1}, {"comment_id": 2}]
        comment_id = 1
        offset = 0
        limit = 2

        mock_storage.is_id_comment.return_value = None
        mock_storage.get_comment_replies.return_value = replies_dto_list
        mock_json_presenter.get_comment_replies_response.return_value = mock_response

        comment_interactor = CommentInteractor(mock_json_presenter,
                                               mock_storage)
        response_from_get_comment_replies = comment_interactor.\
            get_comment_replies(
            comment_id, offset, limit)
        mock_storage.is_id_comment.assert_called_once_with(
            comment_id)
        mock_storage.get_comment_replies.assert_called_once_with(
            comment_id,
            offset, limit)
        mock_json_presenter.get_comment_replies_response.\
            assert_called_once_with(
            replies_dto_list)

        assert response_from_get_comment_replies == mock_response

    def test_get_reply_replies_raises_bad_request(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        comment_id = 1
        offset = 0
        limit = 2
        mock_storage.is_id_comment.side_effect = SuspiciousOperation
        mock_json_presenter.raise_invalid_comment_id.side_effect = BadRequest
        comment_interactor = CommentInteractor(mock_json_presenter,
                                               mock_storage)
        with self.assertRaises(BadRequest):
            comment_interactor.get_comment_replies(comment_id,
                                                   offset, limit)

        mock_storage.is_id_comment.assert_called_once_with(
            comment_id)
        mock_json_presenter.raise_invalid_comment_id.assert_called_once()
