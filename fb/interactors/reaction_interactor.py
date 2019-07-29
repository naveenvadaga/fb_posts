from django.core.exceptions import ObjectDoesNotExist

from .presenters.presenter import Presenter
from .storages.storage import Storage


class ReactionInteractor:

    def __init__(self, presenter: Presenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def react_to_post(self, reacted_by_id: int, post_id: int,
                      reaction_type: str) -> dict:

        try:
            reaction = self.storage.get_post_reaction(reacted_by_id,
                                                      post_id)

            response = self.delete_or_update_post_reaction(reaction,
                                                           reaction_type)
        except ObjectDoesNotExist:
            created_react_id = self.storage.react_to_post(reacted_by_id,
                                                          post_id,
                                                          reaction_type)
            response = self.presenter.create_reaction_response(
                created_react_id)

        return response

    def react_to_comment(self, reacted_by_id: int, comment_id: int,
                         reaction_type: str) -> dict:

        try:
            reaction = self.storage.get_comment_reaction(reacted_by_id,
                                                         comment_id)

            response = self.delete_or_update_comment_reaction(reaction,
                                                              reaction_type)
        except ObjectDoesNotExist:
            created_react_id = self.storage.react_to_comment(reacted_by_id,
                                                             comment_id,
                                                             reaction_type)
            response = self.presenter.create_reaction_response(
                created_react_id)

        return response

    def delete_or_update_comment_reaction(self, reaction,
                                          reaction_type):

        if reaction.reaction_type == reaction_type:
            self.storage.delete_reaction(reaction.id)
            response = self.presenter.create_reaction_response(None)
        else:
            self.storage.update_reaction(reaction.id, reaction_type)
            response = self.presenter.create_reaction_response(
                reaction.id)

        return response

    def delete_or_update_post_reaction(self, reaction,
                                       reaction_type):

        if reaction.reaction_type == reaction_type:
            self.storage.delete_reaction(reaction.id)
            response = self.presenter.create_reaction_response(None)
        else:
            self.storage.update_reaction(reaction.id, reaction_type)
            response = self.presenter.create_reaction_response(
                reaction.id)

        return response
