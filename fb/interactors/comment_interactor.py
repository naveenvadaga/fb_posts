from .presenters.json_presenter import JsonPresenter
from .storages.storage import Storage


class CommentInteractor:
    def __init__(self, presenter: JsonPresenter, storage: Storage):
        self.presenter = presenter
        self.storage = storage

    def add_comment_to_post(self, post_id: int, commenter_id: int, comment_text: str) -> dict:
        created_comment_id = self.storage.add_comment_to_post(post_id, commenter_id, comment_text)
        response = self.presenter.create_comment_response(created_comment_id)
        return response

    def add_comment_to_comment(self, comment_id: int, commenter_id: int, comment_text: str) -> dict:
        comment_reply_id = self.storage.comment_reply_id_field(comment_id)
        if comment_reply_id is None:
            comment_id = self.storage.add_comment_to_comment(comment_id, commenter_id, comment_text)
        else:
            comment_id = self.storage.add_comment_to_comment(comment_reply_id, commenter_id, comment_text)

        response = self.presenter.create_comment_response(comment_id)
        return response
