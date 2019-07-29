import unittest
from unittest.mock import Mock
from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.comment_interactor import CommentInteractor


class TestAddReplyToComment(unittest.TestCase):
    def test_add_reply_to_comment(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        comment_id = 1
        commenter_id = 1
        comment_text = "comment"
        created_comment_id = 2
        mock_response = {"comment_id": created_comment_id}
        mock_storage.get_parent_comment_id.return_value = None
        mock_storage.add_reply_to_comment.return_value = created_comment_id
        mock_json_presenter.create_comment_response.return_value = mock_response

        comment_interactor = CommentInteractor(mock_json_presenter,
                                               mock_storage)
        response_from_get_reactions_count_post = comment_interactor. \
            add_reply_to_comment(
            comment_id, commenter_id,
            comment_text)

        mock_storage.get_parent_comment_id.assert_called_once_with(comment_id)
        mock_storage.add_reply_to_comment.assert_called_once_with(
            comment_id,
            commenter_id,
            comment_text)
        mock_json_presenter.create_comment_response.assert_called_once_with(
            created_comment_id)

        assert response_from_get_reactions_count_post == mock_response

    def test_add_reply_to_reply(
            self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        comment_id = 1
        reply_id = 2
        commenter_id = 1
        comment_text = "comment"
        created_comment_id = 3
        mock_response = {"comment_id": created_comment_id}
        mock_storage.get_parent_comment_id.return_value = 1
        mock_storage.add_reply_to_comment.return_value = created_comment_id
        mock_json_presenter.create_comment_response.return_value = mock_response

        comment_interactor = CommentInteractor(mock_json_presenter,
                                               mock_storage)
        response_from_get_reactions_count_post = comment_interactor.\
            add_reply_to_comment(
            reply_id, commenter_id,
            comment_text)

        mock_storage.get_parent_comment_id.assert_called_once_with(reply_id)
        mock_storage.add_reply_to_comment.assert_called_once_with(
            comment_id,
            commenter_id,
            comment_text)
        mock_json_presenter.create_comment_response.assert_called_once_with(
            created_comment_id)

        assert response_from_get_reactions_count_post == mock_response
