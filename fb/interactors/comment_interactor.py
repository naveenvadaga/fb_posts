from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage
from django.core.exceptions import SuspiciousOperation


class CommentInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def add_comment_to_post_interactor(self, post_id: int, commenter_id: int,
                                       comment_text: str) -> dict:
        created_comment_id = self.storage.add_comment_to_post(post_id,
                                                              commenter_id,
                                                              comment_text)
        response = self.presenter.create_comment_response(created_comment_id)
        return response

    def add_reply_to_comment_interactor(self, comment_id: int, commenter_id: int,
                                        comment_text: str) -> dict:
        parent_comment_id = self.storage.get_parent_comment_id(comment_id)
        if parent_comment_id is None:
            created_comment_id = self.storage.add_reply_to_comment(comment_id,
                                                                   commenter_id,
                                                                   comment_text)
        else:
            created_comment_id = self.storage.add_reply_to_comment(
                parent_comment_id,
                commenter_id,
                comment_text)

        response = self.presenter.create_comment_response(created_comment_id)
        return response

    def get_comment_replies_interactor(self, comment_id: int, offset: int, limit: int):
        try:
            self.storage.is_id_comment(comment_id)
        except SuspiciousOperation:
            self.presenter.raise_invalid_comment_id()
        replies_dto_list = self.storage.get_comment_replies(comment_id, offset,
                                                            limit)
        response = self.presenter.get_comment_replies_response(
            replies_dto_list)
        return response
