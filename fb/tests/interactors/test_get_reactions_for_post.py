import unittest
from unittest.mock import Mock
from fb.interactors.storages.storage import Storage, PersonWithReactionDto
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class TestGetReactionsForPost(unittest.TestCase):

    def test_get_reactions_for_post_returns_reactions_for_post(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)

        mock_reaction1 = Mock(
            spec=[field.name for field in fields(PersonWithReactionDto)])
        mock_reaction2 = Mock(
            [field.name for field in fields(PersonWithReactionDto)])
        mock_reaction_list = [mock_reaction1, mock_reaction2]
        post_id = 1
        offset = 0
        limit = 2

        mock_response = [{'react_type': "haha"}, {'react_type': 'wow'}]
        mock_storage.get_post_reactions.return_value = mock_reaction_list
        mock_json_presenter.create_post_reactions_response.return_value = mock_response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_reactions_count_post = post_interactor. \
            get_post_reactions(post_id, offset, limit)
        mock_storage.get_post_reactions.assert_called_once_with(post_id,
                                                                offset, limit)

        mock_json_presenter.create_post_reactions_response. \
            assert_called_once_with(mock_reaction_list)
        assert response_from_get_reactions_count_post == mock_response
