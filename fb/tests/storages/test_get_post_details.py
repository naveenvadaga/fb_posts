from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestPostDetails:

    @pytest.fixture()
    def post_setup(self, person_fixture, persons_fixture):
        self.posted_person = person_fixture
        self.post_content = "post content"
        self.post = Post.objects.create(person_id=person_fixture.id,
                                        post_content=self.post_content)
        self.react_type1 = "haha"
        self.react_type2 = "wow"
        self.react_type3 = "like"
        self.person1 = persons_fixture[0]
        self.person2 = persons_fixture[1]
        self.person3 = persons_fixture[2]
        self.react1_for_post = React.objects.create(person_id=self.person1.id,
                                                    post_id=self.post.id,
                                                    react_type=self.react_type1)
        self.react2_for_post = React.objects.create(person_id=self.person2.id,
                                                    post_id=self.post.id,
                                                    react_type=self.react_type2)
        self.react3_for_post = React.objects.create(person_id=self.person3.id,
                                                    post_id=self.post.id,
                                                    react_type=self.react_type3)

    @pytest.fixture()
    def post_details_setup(self, post_setup):
        self.comment_content = "comment content"
        self.comment1_for_post = Comment.objects.create(
            person_id=self.person1.id, comment_content=self.comment_content,
            post_id=self.post.id)
        self.comment1_commented_person = self.person1
        self.reaction1_for_comment1 = React.objects.create(
            person_id=self.person1.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.react_type1)
        self.reaction2_for_comment1 = React.objects.create(
            person_id=self.person2.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.react_type2)
        self.reaction3_for_comment1 = React.objects.create(
            person_id=self.person3.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.react_type3)
        self.reply1_for_comment1_content = "reply for comment 1"
        self.reply2_for_comment1_content = "reply2 for comment 1"
        self.reply1_for_comment1 = Comment.objects.create(
            person_id=self.person2.id,
            comment_content=self.reply1_for_comment1_content,
            reply_id=self.comment1_for_post.id)
        self.reply1_commented_person = self.person2
        self.reply2_for_comment1 = Comment.objects.create(
            person_id=self.person3.id,
            comment_content=self.reply2_for_comment1_content,
            reply_id=self.comment1_for_post.id)
        self.reply2_person = self.person3

    def test_get_post_details_post_dto(self, post_details_setup):
        post_id = self.post.id
        storage = StorageClass()
        post_details = storage.get_post_details(post_id)
        post_dto = post_details.post
        posted_person_dto = post_dto.posted_person
        reaction_type_dto = post_details.reactions_types
        reactions_types = {self.react1_for_post.react_type,
                           self.react2_for_post.react_type,
                           self.react3_for_post.react_type}
        reactions_types_count = len(reactions_types)
        assert post_dto.id == post_id
        assert post_dto.post_content == self.post_content
        assert post_dto.posted_at == self.post.posted_at
        assert posted_person_dto.id == self.posted_person.id
        assert posted_person_dto.username == self.posted_person.username
        assert posted_person_dto.profile_url_pic == self.posted_person.profilePicUrl
        assert set(reaction_type_dto.type) == reactions_types
        assert reaction_type_dto.count == reactions_types_count

    def test_get_post_details_comment_dto(self, post_details_setup):
        post_id = self.post.id
        storage = StorageClass()
        post_details = storage.get_post_details(post_id)
        comments_dto = post_details.comments
        setup_reactions_types = {self.reaction1_for_comment1.react_type,
                                 self.reaction2_for_comment1.react_type,
                                 self.reaction3_for_comment1.react_type}
        setup_reactions_types_count = len(setup_reactions_types)
        comments_dict = {}
        comments_dict[self.comment1_for_post.id] = self.comment1_for_post
        comment_dto = comments_dto[0].comment
        setup_comment_dto = None
        if comment_dto.id in comments_dict:
            setup_comment_dto = comments_dict[comment_dto.id]
        assert comment_dto.id == setup_comment_dto.id
        assert comment_dto.commenter.id == setup_comment_dto.person.id
        assert comment_dto.comment_at == setup_comment_dto.comment_at
        assert comment_dto.comment_content == setup_comment_dto.comment_content
        assert set(comment_dto.reactions.type) == setup_reactions_types
        assert comment_dto.reactions.count == setup_reactions_types_count

    def test_get_post_details_replies_dto(self, post_details_setup):
        post_id = self.post.id
        storage = StorageClass()
        post_details = storage.get_post_details(post_id)
        replies_dto = post_details.comments[0].replies
        replies_dict = {}
        replies_dict[self.reply1_for_comment1.id] = self.reply1_for_comment1
        replies_dict[self.reply2_for_comment1.id] = self.reply2_for_comment1
        reply_dto = replies_dto[0]
        setup_reply_dto = None
        if reply_dto.id in replies_dict:
            setup_reply_dto = replies_dict[reply_dto.id]
        assert reply_dto.id == setup_reply_dto.id
        assert reply_dto.commenter.id == setup_reply_dto.person.id
        assert reply_dto.comment_at == setup_reply_dto.comment_at
        assert reply_dto.comment_content == setup_reply_dto.comment_content
        assert reply_dto.reactions.type == []
        assert reply_dto.reactions.count == 0
