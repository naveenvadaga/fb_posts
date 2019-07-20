from .presenters.post_presenter import PostPresenter
from .storages.post_storage import PostStorage
from typing import Dict


class PostInteractor:

    def __init__(self, presenter: PostPresenter, storage: PostStorage):
        self.presenter = presenter
        self.storage = storage

    def create_post_interactor(self, created_by_id: int, post_content: str) -> Dict[str, int]:
        post = self.storage.create_post(created_by_id, post_content)
        response = self.presenter.create_post_response(post)
        return response
