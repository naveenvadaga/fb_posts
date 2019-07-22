import unittest
from unittest.mock import Mock

from django.core.exceptions import ObjectDoesNotExist

from fb.interactors.storages.storage import Storage, ReactDto
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.react_interactor import ReactInteractor
from dataclasses import fields


class TestReactToPost(unittest.TestCase):

    def test_react_to_post_returns_reactions_id(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"
        reaction_id = 1
        response = {"react_id": reaction_id}
        mock_storage.react_to_post_exists.side_effect = ObjectDoesNotExist
        mock_storage.react_to_post.return_value = reaction_id
        mock_json_presenter.create_react_response.return_value = response

        react_interactor = ReactInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post(reacted_by_id, post_id, reaction_type)

        mock_storage.react_to_post_exists.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.react_to_post.assert_called_once_with(reacted_by_id, post_id, reaction_type)
        assert response_from_react_to_post == response

    def test_react_to_post_when_reactions_by_same_person_with_same_reaction_type(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"
        response = {""}
        mock_react_dto = Mock(spec=[field.name for field in fields(ReactDto)])
        mock_react_dto.react_type = "haha"
        mock_storage.react_to_post_exists.return_value = mock_react_dto
        mock_storage.delete_reaction.return_value = None
        mock_json_presenter.create_react_response.return_value = response

        react_interactor = ReactInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post(reacted_by_id, post_id, reaction_type)

        mock_storage.react_to_post_exists.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.delete_reaction.assert_called_once_with(mock_react_dto.id)
        mock_json_presenter.create_react_response.assert_called_once_with(None)
        assert response_from_react_to_post == response

    def test_react_to_post_when_reactions_by_same_person_with_different_reaction_type(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)
        reacted_by_id = 1
        post_id = 1
        reaction_type = "haha"

        mock_react_dto = Mock(spec=[field.name for field in fields(ReactDto)])
        mock_react_dto.id = 1
        response = {"react_id": mock_react_dto.id}
        mock_react_dto.react_type = "wow"
        mock_storage.react_to_post_exists.return_value = mock_react_dto
        mock_storage.update_reaction_type.return_value = mock_react_dto.id
        mock_json_presenter.create_react_response.return_value = response

        react_interactor = ReactInteractor(mock_json_presenter, mock_storage)
        response_from_react_to_post = react_interactor.react_to_post(reacted_by_id, post_id, reaction_type)

        mock_storage.react_to_post_exists.assert_called_once_with(reacted_by_id, post_id)
        mock_storage.update_reaction_type.assert_called_once_with(mock_react_dto.id, reaction_type)
        mock_json_presenter.create_react_response.assert_called_once_with(mock_react_dto.id)
        assert response_from_react_to_post == response
