import unittest
from unittest.mock import Mock

from django.core.exceptions import ObjectDoesNotExist

from fb.interactors.storages.storage import Storage, ReactionDto
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.react_interactor import ReactionInteractor
from dataclasses import fields


class TestReactToPost(unittest.TestCase):

    def test_react_to_post_returns_reactions_id(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"
        reaction_id = 1
        mock_response = {"react_id": reaction_id}
        mock_storage.get_post_reaction.side_effect = ObjectDoesNotExist
        mock_storage.react_to_post_interactor.return_value = reaction_id
        mock_json_presenter.create_reaction_response.return_value = mock_response

        react_interactor = ReactionInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post_interactor(reacted_by_id, post_id, reaction_type)

        mock_storage.get_post_reaction.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.react_to_post_interactor.assert_called_once_with(reacted_by_id, post_id, reaction_type)
        assert response_from_react_to_post == mock_response

    def test_react_to_post_when_reactions_by_same_person_with_same_reaction_type(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"
        mock_response = {""}
        mock_react_dto = Mock(spec=[field.name for field in fields(ReactionDto)])
        mock_react_dto.react_type = "haha"
        mock_storage.get_post_reaction.return_value = mock_react_dto
        mock_storage.delete_reaction.return_value = None
        mock_json_presenter.create_reaction_response.return_value = mock_response

        react_interactor = ReactionInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post_interactor(reacted_by_id, post_id, reaction_type)

        mock_storage.get_post_reaction.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.delete_reaction.assert_called_once_with(mock_react_dto.id)
        mock_json_presenter.create_reaction_response.assert_called_once_with(None)
        assert response_from_react_to_post == mock_response

    def test_react_to_post_when_reactions_by_same_person_with_different_reaction_type(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"

        mock_react_dto = Mock(spec=[field.name for field in fields(ReactionDto)])
        mock_react_dto.id = 1
        mock_response = {"react_id": mock_react_dto.id}
        mock_react_dto.react_type = "wow"
        mock_storage.get_post_reaction.return_value = mock_react_dto
        mock_storage.update_reaction.return_value = mock_react_dto.id
        mock_json_presenter.create_reaction_response.return_value = mock_response

        react_interactor = ReactionInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post_interactor(reacted_by_id, post_id, reaction_type)

        mock_storage.get_post_reaction.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.update_reaction.assert_called_once_with(mock_react_dto.id, reaction_type)
        mock_json_presenter.create_reaction_response.assert_called_once_with(mock_react_dto.id)
        assert response_from_react_to_post == mock_response
