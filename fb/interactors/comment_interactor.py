from .presenters.presenter import Presenter
from .storages.storage import Storage


class CommentInteractor:
    def __init__(self, presenter: Presenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def add_comment_to_post(self, post_id: int, commenter_id: int,
                            comment_text: str) -> dict:

        created_comment_id = self.storage.add_comment_to_post(post_id,
                                                              commenter_id,
                                                              comment_text)

        response = self.presenter.create_comment_response(created_comment_id)

        return response

    def add_reply_to_comment(self, comment_id: int,
                             commenter_id: int,
                             comment_text: str) -> dict:

        parent_comment_id = self.storage.get_parent_comment_id(comment_id)

        if parent_comment_id is None:
            created_comment_id = self.storage.add_reply_to_comment(
                comment_id, commenter_id, comment_text)
        else:
            created_comment_id = self.storage.add_reply_to_comment(
                parent_comment_id,
                commenter_id,
                comment_text)

        response = self.presenter.create_comment_response(created_comment_id)

        return response

    def get_comment_replies(self, comment_id: int, offset: int,
                            limit: int):

        comment = self.storage.is_id_comment(comment_id)

        if not comment:
            self.presenter.raise_invalid_comment_id()
        replies_dto_list = self.storage.get_comment_replies(comment_id, offset,
                                                            limit)
        response = self.presenter.get_comment_replies_response(
            replies_dto_list)

        return response
