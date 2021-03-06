import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage, UserPostDto
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class TestGetPostsPostedByPerson(unittest.TestCase):

    def test_get_user_posts_returns_list_of_posts_details(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)

        person_id = 1
        mock_get_post1_dto = Mock(
            spec=[field.name for field in fields(UserPostDto)])
        mock_get_post2_dto = Mock(
            spec=[field.name for field in fields(UserPostDto)])
        mock_get_post_list = [mock_get_post1_dto, mock_get_post2_dto]
        mock_response = [{"post_id": 1}, {"post_id": 2}]

        mock_storage.get_user_posts.return_value = mock_get_post_list
        mock_json_presenter.get_user_posts_response.return_value = mock_response
        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_posts_posted_by_person = post_interactor.\
            get_user_posts(person_id)

        mock_storage.get_user_posts.assert_called_once_with(person_id)
        mock_json_presenter.get_user_posts_response.assert_called_once_with(
            mock_get_post_list)
        assert response_from_get_posts_posted_by_person == mock_response
