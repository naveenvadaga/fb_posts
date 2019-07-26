from django.core.exceptions import ObjectDoesNotExist

from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage


class ReactInteractor:

    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def react_to_post_interactor(self, reacted_by_id: int, post_id: int,
                                 reaction_type: str) -> dict:
        try:
            existing_react = self.storage.post_reaction_exists_or_not(
                reacted_by_id,
                post_id)
            if existing_react.reaction_type == reaction_type:
                self.storage.delete_reaction(existing_react.id)
                response = self.presenter.create_reaction_response(None)
            else:
                self.storage.update_reaction(existing_react.id,
                                             reaction_type)
                response = self.presenter.create_reaction_response(
                    existing_react.id)

        except ObjectDoesNotExist:
            created_react_id = self.storage.react_to_post(reacted_by_id,
                                                          post_id,
                                                          reaction_type)
            response = self.presenter.create_reaction_response(created_react_id)
        return response

    def react_to_comment_interactor(self, reacted_by_id: int, comment_id: int,
                                    reaction_type: str) -> dict:
        try:
            existing_react = self.storage.comment_reaction_exists_or_not(
                reacted_by_id,
                comment_id)
            if existing_react.reaction_type == reaction_type:
                self.storage.delete_reaction(existing_react.id)
                response = self.presenter.create_reaction_response(None)
            else:
                self.storage.update_reaction(existing_react.id,
                                             reaction_type)
                response = self.presenter.create_reaction_response(
                    existing_react.id)

        except ObjectDoesNotExist:
            created_react_id = self.storage.react_to_comment(reacted_by_id,
                                                             comment_id,
                                                             reaction_type)
            response = self.presenter.create_reaction_response(created_react_id)
        return response
