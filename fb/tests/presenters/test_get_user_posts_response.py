import unittest
from fb.presenters.json_presenter import *
from freezegun import freeze_time
from datetime import datetime


class TestGetUserPosts(unittest.TestCase):
    @freeze_time("2012-01-14 12:00:01")
    def post_details_set_up(self):
        person_dto_1 = PersonDto(1, "username1",
                                 "https://www.profile_url_pic.com")
        person_dto_2 = PersonDto(2, "username2",
                                 "https://www.profile_url_pic.com")
        person_dto_3 = PersonDto(3, "username3",
                                 "https://www.profile_url_pic.com")

        reaction_dto_1 = ReactionDto("haha", 1, 2, post_id=1)
        reaction_dto_2 = ReactionDto("wow", 2, 3, post_id=1)
        comment_dto = CommentDto(1, 2, datetime.now(), "comment 1", post_id=1)

        comment_dto_list = [comment_dto]
        reaction_dto_list = [reaction_dto_1, reaction_dto_2]
        person_dto_list = [person_dto_1, person_dto_2, person_dto_3]
        post_dto = PostDto(1, 1, "post 1", datetime.now())

        self.user_post_dto = UserPostDto(post_dto, person_dto_list,
                                         reaction_dto_list, comment_dto_list)
        self.user_post_dto_list = [self.user_post_dto]

    def test_post_details(self):
        self.post_details_set_up()

        json_presenter = JsonPresenter()
        response = \
            json_presenter.get_user_posts_response(self.user_post_dto_list)[0]

        post_dto = self.user_post_dto.post
        person_dto = None
        for person in self.user_post_dto.persons:
            if person.id == response['posted_by']['id']:
                person_dto = person

        assert response['post_id'] == post_dto.id
        assert response['posted_at'] == post_dto.posted_at.strftime(
            "%Y-%m-%d %H:%M:%S")
        assert response['post_content'] == post_dto.post_content
        assert response['posted_by']['id'] == person_dto.id
        assert response['posted_by']['username'] == person_dto.username
        assert response['posted_by'][
                   'profile_pic_url'] == person_dto.profile_url_pic

    def test_comment_stats(self):
        self.post_details_set_up()

        json_presenter = JsonPresenter()
        response = \
            json_presenter.get_user_posts_response(self.user_post_dto_list)[0]

        comments_list = response['comments']
        response_comment = comments_list[0]
        comment_dto = None
        person_dto = None
        for comment in self.user_post_dto.comments:
            if comment.comment_id == response_comment['comment_id']:
                comment_dto = comment
        for person in self.user_post_dto.persons:
            if person.id == response_comment['commenter']['id']:
                person_dto = person

        assert response_comment['comment_id'] == comment_dto.comment_id
        assert response_comment[
                   'commented_at'] == comment_dto.commented_at.strftime(
            "%Y-%m-%d %H:%M:%S")
        assert response_comment[
                   'comment_content'] == comment_dto.comment_content
        assert response_comment['commenter']['id'] == person_dto.id
        assert response_comment['commenter']['username'] == person_dto.username
        assert response_comment['commenter'][
                   'profile_pic_url'] == person_dto.profile_url_pic

    def test_reaction_stats(self):
        self.post_details_set_up()

        json_presenter = JsonPresenter()
        response = \
            json_presenter.get_user_posts_response(self.user_post_dto_list)[0]

        reaction_dto_list = self.user_post_dto.reactions
        comments_list = response['comments']
        response_comment = comments_list[0]
        post_reaction_types = []
        comment_reaction_types = []

        for reaction in reaction_dto_list:
            if reaction.post_id == response['post_id']:
                post_reaction_types.append(reaction.reaction_type)
            if reaction.comment_id == response_comment['comment_id']:
                comment_reaction_types.append(reaction.reaction_type)

        assert response['reactions']['type'] == post_reaction_types
        assert response['reactions']['count'] == len(post_reaction_types)
        assert response_comment['reactions']['type'] == comment_reaction_types
        assert response_comment['reactions']['count'] == len(
            comment_reaction_types)
