import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage, GetPostDto
from fb.interactors.presenters.json_presenter import JsonPresenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class TestGetPostsPostedByPerson(unittest.TestCase):

    def test_get_posts_posted_by_person_returns_list_of_posts_details(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=JsonPresenter)

        person_id = 1
        mock_get_post1_dto = Mock(spec=[field.name for field in fields(GetPostDto)])
        mock_get_post2_dto = Mock(spec=[field.name for field in fields(GetPostDto)])
        mock_get_post_list = [mock_get_post1_dto, mock_get_post2_dto]
        mock_response = [{"post_id": 1}, {"post_id": 2}]

        mock_storage.get_posts_posted_by_person.return_value = mock_get_post_list
        mock_json_presenter.get_posts_posted_by_person_response.return_value = mock_response
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_posts_posted_by_person = post_interactor.get_posts_posted_by_person(
            person_id)

        mock_storage.get_posts_posted_by_person.assert_called_once_with(person_id)
        mock_json_presenter.get_posts_posted_by_person_response.assert_called_once_with(
            mock_get_post_list)
        assert response_from_get_posts_posted_by_person == mock_response
