import unittest
from fb.presenters.json_presenter import *
from freezegun import freeze_time


class TestCreatePost(unittest.TestCase):
    @freeze_time("2012-01-14 12:00:01")
    def test_create_post_reactions_response(self):
        reaction_dto_1 = ReactionDto("haha", 1, 1, 1)
        reaction_dto_2 = ReactionDto("like", 1, 1, 1)
        reaction_dto_3 = ReactionDto("wow", 1, 1, 1)
        person_with_reaction_dto_1 = PersonWithReactionDto(1, "username1", "https://www.profilePic.com", reaction_dto_1)
        person_with_reaction_dto_2 = PersonWithReactionDto(2, "username2", "https://www.profilePic.com", reaction_dto_2)
        person_with_reaction_dto_3 = PersonWithReactionDto(3, "username3", "https://www.profilePic.com", reaction_dto_3)
        person_with_reaction_dto_list = [person_with_reaction_dto_1, person_with_reaction_dto_2,
                                         person_with_reaction_dto_3]
        dto_dict = {person_with_reaction_dto_1.id: person_with_reaction_dto_1,
                    person_with_reaction_dto_2.id: person_with_reaction_dto_2,
                    person_with_reaction_dto_3.id: person_with_reaction_dto_3}
        presenter = Presenter()
        response = presenter.create_post_reactions_response(person_with_reaction_dto_list)
        reactions_response_list = response['reactions']
        response_reaction = reactions_response_list[0]
        reaction_details_dto = dto_dict[response_reaction['id']]
        assert response_reaction['id'] in dto_dict
        assert response_reaction['username'] == reaction_details_dto.username
        assert response_reaction['profile_pic_url'] == reaction_details_dto.profile_url_pic
        assert response_reaction['reaction_type'] == reaction_details_dto.reaction.reaction_type
