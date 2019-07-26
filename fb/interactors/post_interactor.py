from django.core.exceptions import ObjectDoesNotExist

from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage
from typing import Dict, List


class PostInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def create_post_interactor(self, created_by_id: int, post_content: str) -> \
            Dict[str, int]:
        created_post = self.storage.create_post(created_by_id, post_content)
        response = self.presenter.create_post_response(created_post)
        return response

    def delete_post_interactor(self, post_id: int) -> dict:
        try:
            self.storage.delete_post(post_id)

        except ObjectDoesNotExist:
            self.presenter.raise_invalid_post_id()
        response = self.presenter.delete_post_response()
        return response

    def get_post_reactions_count_interactor(self) -> dict:
        count = self.storage.get_total_post_reactions_count()
        response = self.presenter.get_post_reactions_count_response(count)
        return response

    def get_user_reacted_posts_interactor(self, user_id: int) -> dict:
        post_ids_list = self.storage.get_user_reacted_post_ids(user_id)
        response = self.presenter.get_user_reacted_posts_response(
            post_ids_list)
        return response

    def get_post_metrics_interactor(self, post_id: int) -> dict:
        post_metrics_dto_list = self.storage.get_post_reaction_metrics(post_id)
        response = self.presenter.get_post_metrics_response(
            post_metrics_dto_list)
        return response

    def get_more_positive_reacted_post_ids_interactor(self) -> dict:
        positive_reacted_post_list = self.storage.get_more_positive_reacted_post_ids()
        response = self.presenter.get_positive_reacted_posts_response(
            positive_reacted_post_list)
        return response

    def get_post_details_interactor(self, post_id: int) -> dict:
        get_post_dto = self.storage.get_post_details(post_id)
        response = self.presenter.get_post_details_response(get_post_dto)
        return response

    def get_user_posts_interactor(self, person_id: int, offset: int,
                                  limit: int) -> List[dict]:
        post_dto_list = self.storage.get_user_posts(person_id,
                                                    offset, limit)
        response = self.presenter.get_user_posts_response(
            post_dto_list)
        return response

    def get_post_reactions_interactor(self, post_id: int, offset: int,
                                      limit: int) -> dict:
        reactions_dto_list = self.storage.get_post_reactions(post_id, offset,
                                                             limit)
        response = self.presenter.create_post_reactions_response(
            reactions_dto_list)
        return response
