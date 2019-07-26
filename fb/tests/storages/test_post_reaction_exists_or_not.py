from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import StorageClass
import pytest


@pytest.mark.django_db
class TestReactToPostExistsOrNot:

    def test_post_reaction_exists_or_not_returns_react_dto(self,
                                                           react_to_post_fixture):
        storage = StorageClass()
        react_dto = storage.post_reaction_exists_or_not(
            react_to_post_fixture.person.id, react_to_post_fixture.id)
        assert react_dto.id == react_to_post_fixture.id
        assert react_dto.reaction_type == react_to_post_fixture.react_type
        assert react_dto.reacted_person_id == react_to_post_fixture.person.id
        assert react_dto.post_id == react_to_post_fixture.post.id

    def test_post_reaction_exists_or_not_raises_exception(self):
        storage = StorageClass()
        with pytest.raises(ObjectDoesNotExist):
            storage.post_reaction_exists_or_not(1, 1)
