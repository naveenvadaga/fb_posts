from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage
from typing import Dict


class GetMethodsOnPostInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def get_reactions_for_posts_interactor(self) -> dict:
        count = self.storage.get_reactions_count_to_posts()
        response = self.presenter.get_reactions_count_for_posts_response(count)
        return response

    def get_post_reacted_by_user_interactor(self, user_id: int) -> dict:
        post_ids_list = self.storage.get_post_reacted_by_user(user_id)
        response = self.presenter.get_post_reacted_by_user_response(post_ids_list)
        return response

    def get_post_metrics_interactor(self, post_id: int) -> dict:
        post_metrics = self.storage.get_post_metrics(post_id)
        response = self.presenter.get_post_metrics_response(post_metrics)
        return response

    def get_positive_reacted_posts_interactor(self) -> dict:
        positive_reacted_post = self.storage.get_positive_reacted_posts()
        response = self.presenter.get_positive_reacted_posts_response(positive_reacted_post)
        return response

    def get_post_details(self, post_id: int) -> dict:
        get_post_dto = self.storage.get_post_details(post_id)
        response = self.presenter.get_post_details_response(get_post_dto)
        return response

    def get_posts_posted_by_person(self, person_id: int) -> dict:
        post_dto_list = self.storage.get_posts_posted_by_person(person_id)
        response = self.presenter.get_posts_posted_by_person_response(post_dto_list)
        return response
