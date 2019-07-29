from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import StorageImplementer
import pytest


@pytest.mark.django_db
class TestReactToCommentExistsOrNot:

    def test_get_comment_reaction_returns_reaction_dto(self,
                                                       react_to_comment_fixture):
        storage = StorageImplementer()
        reaction_dto = storage.get_comment_reaction(
            react_to_comment_fixture.person_id,
            react_to_comment_fixture.id)

        assert reaction_dto.id == react_to_comment_fixture.id
        assert reaction_dto.reaction_type == react_to_comment_fixture.react_type
        assert reaction_dto.reacted_person_id == react_to_comment_fixture.person_id
        assert reaction_dto.comment_id == react_to_comment_fixture.comment_id

    def test_get_comment_reaction_raises_exception(self):
        storage = StorageImplementer()

        with pytest.raises(ObjectDoesNotExist):
            storage.get_post_reaction(1, 1)
