import unittest
from unittest.mock import Mock
from fb.interactors.storages.storage import Storage
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.comment_interactor import CommentInteractor


class TestAddCommentToPost(unittest.TestCase):
    def test_add_comment_to_post_returns_comment_id(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        post_id = 1
        comment_id = 1
        commenter_id = 1
        comment_text = "comment"
        mock_response = {"comment_id": comment_id}
        mock_storage.add_comment_to_post.return_value = comment_id
        mock_json_presenter.create_comment_response.return_value = mock_response

        comment_interactor = CommentInteractor(mock_json_presenter,
                                               mock_storage)
        response_from_get_reactions_count_post = comment_interactor.add_comment_to_post(
            post_id, commenter_id,
            comment_text)

        mock_storage.add_comment_to_post.assert_called_once_with(post_id,
                                                                 commenter_id,
                                                                 comment_text)
        mock_json_presenter.create_comment_response.assert_called_once_with(
            comment_id)
        assert response_from_get_reactions_count_post == mock_response
