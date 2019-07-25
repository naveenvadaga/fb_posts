from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestGetReactionsToPost:

    @pytest.fixture()
    def reactions_setup(self, persons_fixture, post_fixture):
        self.post_id = post_fixture.id
        self.react_type1 = "haha"
        self.react_type2 = "wow"
        self.react_type3 = "like"
        self.react_type4 = "sad"
        person1 = persons_fixture[0]
        person2 = persons_fixture[1]
        person3 = persons_fixture[2]
        person4 = persons_fixture[3]
        self.react1 = Reaction.objects.create(person_id=person1.id,
                                              post_id=self.post_id,
                                              react_type=self.react_type1)
        self.react2 = Reaction.objects.create(person_id=person2.id,
                                              post_id=self.post_id,
                                              react_type=self.react_type2)
        self.react3 = Reaction.objects.create(person_id=person3.id,
                                              post_id=self.post_id,
                                              react_type=self.react_type3)
        self.react4 = Reaction.objects.create(person_id=person4.id,
                                              post_id=self.post_id,
                                              react_type=self.react_type4)

    def test_get_reactions_to_post_returns_first_two_reactions(self,
                                                               reactions_setup):
        setup_reactions_dict = {}
        setup_reactions_dict[self.react1.id] = self.react1
        setup_reactions_dict[self.react2.id] = self.react2
        setup_reactions_dict[self.react3.id] = self.react3
        setup_reactions_dict[self.react4.id] = self.react4
        storage = StorageClass()
        replies_list = storage.get_post_reactions(self.post_id, 0, 2)
        response_reaction = replies_list[0]
        assert len(replies_list) == 2
        setup_reaction = setup_reactions_dict[response_reaction.id]
        assert response_reaction.id == setup_reaction.id
        assert response_reaction.username == setup_reaction.person.username
        assert response_reaction.profile_url_pic == setup_reaction.person.profilePicUrl
        assert response_reaction.reaction_type == setup_reaction.react_type
