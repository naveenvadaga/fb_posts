from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestUserPostsDetails:

    @pytest.fixture()
    def post_setup(self, person_fixture, persons_fixture):
        self.posted_person = person_fixture
        self.post_content = "post content"
        self.post = Post.objects.create(person_id=person_fixture.id,
                                        post_content=self.post_content)
        self.reaction_type1 = "haha"
        self.reaction_type2 = "wow"
        self.reaction_type3 = "like"
        self.person1 = persons_fixture[0]
        self.person2 = persons_fixture[1]
        self.person3 = persons_fixture[2]
        self.person_dict = {person_fixture.id: person_fixture,
                            self.person1.id: self.person1,
                            self.person2.id: self.person2,
                            self.person3.id: self.person3}
        self.reactions1_for_post = Reaction.objects.create(
            person_id=self.person1.id,
            post_id=self.post.id,
            react_type=self.reaction_type1)
        self.reactions2_for_post = Reaction.objects.create(
            person_id=self.person2.id,
            post_id=self.post.id,
            react_type=self.reaction_type2)
        self.reactions3_for_post = Reaction.objects.create(
            person_id=self.person3.id,
            post_id=self.post.id,
            react_type=self.reaction_type3)
        self.reactions_dict = {
            self.reactions1_for_post.id: self.reactions1_for_post,
            self.reactions2_for_post.id: self.reactions3_for_post,
            self.reactions3_for_post.id: self.reactions3_for_post}

    @pytest.fixture()
    def post_details_setup(self, post_setup):
        self.comment_content = "comment content"
        self.comment1_for_post = Comment.objects.create(
            person_id=self.person1.id, comment_content=self.comment_content,
            post_id=self.post.id)
        self.comment1_commented_person = self.person1
        self.reaction1_for_comment1 = Reaction.objects.create(
            person_id=self.person1.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.reaction_type1)
        self.reaction2_for_comment1 = Reaction.objects.create(
            person_id=self.person2.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.reaction_type2)
        self.reaction3_for_comment1 = Reaction.objects.create(
            person_id=self.person3.id,
            comment_id=self.comment1_for_post.id,
            react_type=self.reaction_type3)
        self.reactions_dict[
            self.reaction1_for_comment1.id] = self.reaction1_for_comment1
        self.reactions_dict[
            self.reaction2_for_comment1.id] = self.reaction2_for_comment1
        self.reactions_dict[
            self.reaction3_for_comment1.id] = self.reaction3_for_comment1

    @pytest.fixture()
    def comment_details_setup(self,post_details_setup):
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
        self.comment_dict = {self.comment1_for_post.id: self.comment1_for_post,
                             self.reply1_for_comment1.id: self.reply1_for_comment1,
                             self.reply2_for_comment1.id: self.reply2_for_comment1}


    def test_get_user_posts_dto(self, comment_details_setup):

        storage = StorageImplementer()
        post_details_list = storage.get_user_posts(
            self.posted_person.id, 0, 1)

        post_details = post_details_list[0]
        post_dto = post_details.post

        assert post_dto.id == self.post.id
        assert post_dto.post_content == self.post.post_content
        assert post_dto.posted_at == self.post.posted_at
        assert post_dto.posted_person_id in self.person_dict

    def test_get_user_posts_comments_dto(self, comment_details_setup):

        storage = StorageImplementer()
        post_details_list = storage.get_user_posts(
            self.posted_person.id, 0, 1)

        post_details = post_details_list[0]
        person_dto = post_details.persons[0]
        setup_person_details = None

        if person_dto.id in self.person_dict:
            setup_person_details = self.person_dict[person_dto.id]

        assert len(post_details.persons) == len(self.person_dict)
        assert person_dto.id in self.person_dict
        assert person_dto.username == setup_person_details.username
        assert person_dto.profile_url_pic == setup_person_details.profilePicUrl
        assert person_dto.id == setup_person_details.id

    def test_get_user_posts_comments_replies_dto(self, comment_details_setup):

        storage = StorageImplementer()
        post_details_list = storage.get_user_posts(
            self.posted_person.id, 0, 1)

        post_details = post_details_list[0]
        comments_dto = post_details.comments
        setup_comment_details = None
        comment_dto = comments_dto[0]

        if comment_dto.comment_id in self.comment_dict:
            setup_comment_details = self.comment_dict[comment_dto.comment_id]

        assert len(comments_dto) == len(self.comment_dict)
        assert comment_dto.comment_id == setup_comment_details.id
        assert comment_dto.comment_content == setup_comment_details.comment_content
        assert comment_dto.commenter_id == setup_comment_details.person_id
        assert comment_dto.commented_at == setup_comment_details.comment_at
