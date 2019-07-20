from django.core.exceptions import ObjectDoesNotExist
from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage
from typing import Dict


class PostInteractor:

    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def post_interactor(self, created_by_id: int, post_content: str) -> Dict[str, int]:
        post = self.storage.create_post(created_by_id, post_content)
        response = self.presenter.create_post_response(post)
        return response

    def delete_post_interactor(self, post_id: int) -> dict:
        try:
            self.storage.delete_post(post_id)
            response = self.presenter.delete_post_response()
        except ObjectDoesNotExist:
            response = self.presenter.bad_request_invalid_post_id()
        return response
