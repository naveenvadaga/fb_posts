from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import StorageClass
import pytest


@pytest.mark.django_db
class TestReactToPostExistsOrNot:

    def test_react_to_post_exists_or_not_returns_react_dto(self,
                                                           react_to_post_fixture):
        storage = StorageClass()
        react_dto = storage.react_to_post_exists_or_not(
            react_to_post_fixture.person.id, react_to_post_fixture.id)
        assert react_dto.id == react_to_post_fixture.id
        assert react_dto.react_type == react_to_post_fixture.react_type
        assert react_dto.reacted_person == react_to_post_fixture.person.id
        assert react_dto.post == react_to_post_fixture.post.id

    def test_react_to_post_exists_or_not_raises_exception(self):
        storage = StorageClass()
        with pytest.raises(ObjectDoesNotExist):
            storage.react_to_post_exists_or_not(1, 1)
