from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import StorageImplementer
import pytest


@pytest.mark.django_db
class TestReactToPostExistsOrNot:

    def test_get_post_reaction_returns_reaction_dto(self,
                                                 react_to_post_fixture):
        storage = StorageImplementer()
        react_dto = storage.get_post_reaction(
            react_to_post_fixture.person.id, react_to_post_fixture.id)

        assert react_dto.id == react_to_post_fixture.id
        assert react_dto.reaction_type == react_to_post_fixture.react_type
        assert react_dto.reacted_person_id == react_to_post_fixture.person.id
        assert react_dto.post_id == react_to_post_fixture.post.id

    def test_get_post_reaction_raises_exception(self):
        storage = StorageImplementer()
        with pytest.raises(ObjectDoesNotExist):
            storage.get_post_reaction(1, 1)
