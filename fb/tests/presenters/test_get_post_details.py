import unittest
from fb.presenters.json_presenter import *
from freezegun import freeze_time
from datetime import datetime


class TestGetPostDetails(unittest.TestCase):
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

    def get_post_utilities_setup(self):
        self.post_details_set_up()
        person_dto_list = self.user_post_dto.persons
        self.persons_dict = {}
        for person_dto in person_dto_list:
            self.persons_dict[person_dto.id] = {
                "username": person_dto.username,
                "id": person_dto.id,
                "profile_pic_url": person_dto.profile_url_pic}
        reaction_dto_list = self.user_post_dto.reactions
        self.comment_wise_reactions_stats_dict = {}
        for reaction in reaction_dto_list:
            try:
                self.comment_dict_insert_record(reaction)
            except KeyError:
                self.comment_dict_create_record(reaction)
        self.comment_dict = self.get_comments_dict(self.user_post_dto.comments,
                                                   self.persons_dict,
                                                   self.comment_wise_reactions_stats_dict)

    def get_comments_dict(self, comments_dto, persons_dict,
                          comments_reactions_dict):
        comments_dict = {}
        for comment in comments_dto:
            comment_dict = self.get_comment_dict(comment, persons_dict,
                                                 comments_reactions_dict)
            comments_dict[comment.comment_id] = comment_dict
        return comments_dict

    def get_comment_dict(self, comment, persons_dict, comments_reactions_dict):
        comment_dict = {"comment_id": comment.comment_id,
                        "commenter": persons_dict[comment.commenter_id],
                        "commented_at": comment.commented_at.strftime(
                            "%Y-%m-%d, %H:%M:%S"),
                        "comment_content": comment.comment_content}
        if comment.comment_id in comments_reactions_dict:
            comment_dict["reactions"] = comments_reactions_dict[
                comment.comment_id]
        else:
            comment_dict["reactions"] = {
                "count": 0,
                "type": []
            }
        return comment_dict

    def comment_dict_insert_record(self, reaction):
        self.comment_wise_reactions_stats_dict[reaction.comment_id]["count"] = \
            self.comment_wise_reactions_stats_dict[
                reaction.comment_id][
                "count"] + 1
        self.comment_wise_reactions_stats_dict[reaction.comment_id][
            "type"].append(reaction.reaction_type)

    def comment_dict_create_record(self, reaction):
        self.comment_wise_reactions_stats_dict[reaction.comment_id] = {
            "count": 1,
            "type": [reaction.reaction_type]
        }

    def test_post_details(self):
        self.post_details_set_up()
        json_presenter = JsonPresenter()
        response = json_presenter.get_post_details_response(self.user_post_dto)
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
        response = json_presenter.get_post_details_response(self.user_post_dto)
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
        response = json_presenter.get_post_details_response(self.user_post_dto)
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

    def test_person_dict(self):
        self.get_post_utilities_setup()
        person_dto_list = self.user_post_dto.persons
        json_presenter = JsonPresenter()
        response = json_presenter.get_all_persons_dict(person_dto_list)
        print(response)
        print(self.persons_dict)

        assert response == self.persons_dict

    def test_comment_wise_reaction_stats_dict(self):
        self.get_post_utilities_setup()
        reaction_dto_list = self.user_post_dto.reactions
        json_presenter = JsonPresenter()
        comment_wise_dict = json_presenter.get_comment_wise_reaction_stats_dict(
            reaction_dto_list)

        assert comment_wise_dict == self.comment_wise_reactions_stats_dict

    def test_get_comment_dict(self):
        self.get_post_utilities_setup()
        reaction_dto_list = self.user_post_dto.reactions
        person_dto_list = self.user_post_dto.persons
        comment_dto_list = self.user_post_dto.comments
        comment_dto = comment_dto_list[0]
        json_presenter = JsonPresenter()
        response = json_presenter.get_comment_with_reactions_dict(comment_dto,
                                                                  person_dto_list,
                                                                  reaction_dto_list)

        assert response['comment_id'] == comment_dto.comment_id
        assert response['commented_at'] == comment_dto.commented_at.strftime(
            "%Y-%m-%d %H:%M:%S")
        assert response['comment_content'] == comment_dto.comment_content
        assert response['reactions']['count'] == 0
        assert response['reactions']['type'] == []

    def test_get_comments_details_dict(self):
        self.get_post_utilities_setup()
        comment_dto_list = self.user_post_dto.comments
        json_presenter = JsonPresenter()
        response = json_presenter.get_comment_list(comment_dto_list,
                                                   self.comment_dict)
        comment = response[0]
        setup_comment = self.comment_dict[comment['comment_id']]

        assert len(response) == 1
        assert comment['comment_id'] == setup_comment['comment_id']
        assert comment['commenter']['id'] == setup_comment['commenter'][
            'id']
        assert comment['commented_at'] == setup_comment['commented_at']
        assert comment['comment_content'] == setup_comment['comment_content']
