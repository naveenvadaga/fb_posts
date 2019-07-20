from .storages.storage import Storage
from .presenters.json_presenter import JsonPresenter


class ReactionsForPostInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def get_reactions_for_post(self, post_id: int, offset: int, limit: int) -> dict:
        reactions_list = self.storage.get_reactions_to_post(post_id, offset, limit)
        response = self.presenter.create_reactions_for_post_response(reactions_list)
        return response
