from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestGetCommentReplies:

    @pytest.fixture()
    def replies_setup(self, person_fixture, comment_fixture):
        self.comment_id = comment_fixture.id
        reply_content1 = "comment 1"
        reply_content2 = "comment 2"
        reply_content3 = "comment 3"
        reply_content4 = "comment 4"

        self.reply1 = Comment.objects.create(person_id=person_fixture.id,
                                             comment_content=reply_content1,
                                             reply_id=self.comment_id)
        self.reply2 = Comment.objects.create(person_id=person_fixture.id,
                                             comment_content=reply_content2,
                                             reply_id=self.comment_id)
        self.reply3 = Comment.objects.create(person_id=person_fixture.id,
                                             comment_content=reply_content3,
                                             reply_id=self.comment_id)
        self.reply4 = Comment.objects.create(person_id=person_fixture.id,
                                             comment_content=reply_content4,
                                             reply_id=self.comment_id)

    def test_returns_first_two_replies(self, replies_setup):
        response_dict = {}
        response_dict[self.reply1.id] = self.reply1
        response_dict[self.reply2.id] = self.reply2
        response_dict[self.reply3.id] = self.reply3
        response_dict[self.reply4.id] = self.reply4

        storage = StorageImplementer()
        replies_list = storage.get_comment_replies(self.comment_id, 0, 2)

        response = replies_list[0]
        response_comment = response.comment
        response_person = response.person
        setup_comment = response_dict[response_comment.comment_id]

        assert len(replies_list) == 2
        assert response_comment.comment_id == setup_comment.id
        assert response_comment.commented_at == setup_comment.comment_at
        assert response_comment.comment_content == setup_comment.comment_content
        assert response_person.id == setup_comment.person.id
        assert response_person.username == setup_comment.person.username
        assert response_person.profile_url_pic == setup_comment.person.profilePicUrl
