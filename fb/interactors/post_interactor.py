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
