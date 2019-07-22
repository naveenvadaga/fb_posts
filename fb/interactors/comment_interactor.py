from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage
from django.core.exceptions import SuspiciousOperation


class CommentInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def add_comment_to_post(self, post_id: int, commenter_id: int, comment_text: str) -> dict:
        created_comment_id = self.storage.add_comment_to_post(post_id, commenter_id, comment_text)
        response = self.presenter.create_comment_response(created_comment_id)
        return response

    def add_comment_to_comment(self, comment_id: int, commenter_id: int, comment_text: str) -> dict:
        parent_comment_id = self.storage.comment_reply_id_field(comment_id)
        if parent_comment_id is None:
            comment_id = self.storage.add_comment_to_comment(comment_id, commenter_id, comment_text)
        else:
            comment_id = self.storage.add_comment_to_comment(parent_comment_id, commenter_id, comment_text)

        response = self.presenter.create_comment_response(comment_id)
        return response

    def get_comment_replies(self, comment_id: int, offset: int, limit: int):
        try:
            self.storage.get_comment_with_comment_id_and_reply(comment_id)

        except SuspiciousOperation:
            self.presenter.bad_request_invalid_comment_id()
        replies = self.storage.get_comment_replies(comment_id, offset, limit)
        response = self.presenter.get_replies_for_comment_response(replies)
        return response
