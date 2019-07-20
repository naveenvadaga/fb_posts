from django.core.exceptions import SuspiciousOperation

from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage


class GetMethodsOnCommentInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def get_comment_replies(self, comment_id: int, offset: int, limit: int):
        try:
            self.storage.get_comment_with_comment_id_and_reply(comment_id)
            replies = self.storage.get_comment_replies(comment_id, offset, limit)
            response = self.presenter.get_replies_for_comment_response(replies)
        except SuspiciousOperation:
            response = self.bad_request_invalid_comment_id()

        return response
