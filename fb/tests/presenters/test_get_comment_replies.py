import unittest

from django_swagger_utils.drf_server.exceptions import BadRequest

from fb.presenters.json_presenter import *
from freezegun import freeze_time
from datetime import datetime


class TestGetCommentReplies(unittest.TestCase):

    @freeze_time("2012-01-14 12:00:01")
    def test_comment_replies(self):
        person_dto = PersonDto(1, "username", "https://www.profilepicurl.com")
        reply_dto_1 = CommentDto(1, 1, datetime.now(), "comment1",
                                 commented_on_id=1)
        reply_dto_2 = CommentDto(2, 1, datetime.now(), "comment2",
                                 commented_on_id=2)
        reply_dto_3 = CommentDto(3, 1, datetime.now(), "comment3",
                                 commented_on_id=3)

        comment_with_person_dto_list = [
            CommentWithPersonDto(reply_dto_1, person_dto),
            CommentWithPersonDto(reply_dto_2, person_dto),
            CommentWithPersonDto(reply_dto_3, person_dto)]
        json_presenter = JsonPresenter()
        response = json_presenter.get_comment_replies_response(
            comment_with_person_dto_list)
        replies_response = response['replies']
        reply_response = {}

        for reply in replies_response:
            if reply['comment_id'] == reply_dto_1.comment_id:
                reply_response = reply

        assert len(replies_response) == 3
        assert reply_response['comment_id'] == reply_dto_1.comment_id
        assert reply_response['commented_at'] == reply_dto_1.commented_at
        assert reply_response['comment_content'] == reply_dto_1.comment_content
        assert reply_response['commenter']['username'] == person_dto.username
        assert reply_response['commenter']['id'] == person_dto.id
        assert reply_response['commenter'][
                   'profile_pic_url'] == person_dto.profile_url_pic

    def test_raise_invalid_comment_id_raise_exception(self):
        json_presenter = JsonPresenter()

        with self.assertRaises(BadRequest):
            json_presenter.raise_invalid_comment_id()
