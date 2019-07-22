import unittest
from unittest.mock import Mock
from fb.interactors.storages.storage import Storage, ReactionsForPostDto
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class GetReactionsForPost(unittest.TestCase):

    def test_get_reactions_for_post_returns_reactions_for_post(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)

        mock_reaction1 = Mock(spec=[field.name for field in fields(ReactionsForPostDto)])
        mock_reaction2 = Mock([field.name for field in fields(ReactionsForPostDto)])
        mock_reaction_list = [mock_reaction1, mock_reaction2]
        post_id = 1
        offset = 0
        limit = 2
        response = [{'react_type': "haha"}, {'react_type': 'wow'}]

        mock_storage.get_reactions_to_post.return_value = mock_reaction_list
        mock_json_presenter.create_reactions_for_post_response.return_value = response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_reactions_count_post = post_interactor.get_reactions_for_post(post_id, offset, limit)

        mock_storage.get_reactions_to_post.assert_called_once_with(post_id, offset, limit)
        mock_json_presenter.create_reactions_for_post_response.assert_called_once_with(mock_reaction_list)
        assert response_from_get_reactions_count_post == response
