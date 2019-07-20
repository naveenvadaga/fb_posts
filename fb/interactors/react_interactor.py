from django.core.exceptions import ObjectDoesNotExist

from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage


class ReactInteractor:

    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def react_to_post(self, reacted_by_id: int, post_id: int, reaction_type: str) -> dict:
        try:
            react = self.storage.react_to_post_exists(reacted_by_id, post_id)
            if react.react_type == reaction_type:
                self.storage.delete_reaction(react.id)
                response = None
            else:
                self.storage.update_reaction_type(react.id, reaction_type)
                response = self.presenter.create_react_response(react.id)

        except ObjectDoesNotExist:
            react_id = self.storage.react_to_post(reacted_by_id, post_id, reaction_type)
            response = self.presenter.create_react_response(react_id)
        return response

    def react_to_comment(self, reacted_by_id: int, comment_id: int, reaction_type: str) -> dict:
        try:
            react = self.storage.react_to_comment_exits(reacted_by_id, comment_id)
            if react.react_type == reaction_type:
                self.presenter.create_react_response(self.storage.delete_reaction(react.id))
                response = None
            else:
                self.storage.update_reaction_type(react.id, reaction_type)
                response = self.presenter.create_react_response(react.id)

        except ObjectDoesNotExist:
            react_id = self.storage.react_to_comment(reacted_by_id, comment_id, reaction_type)
            response = self.presenter.create_react_response(react_id)
        return response
