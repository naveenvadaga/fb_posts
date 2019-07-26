from django.core.exceptions import ObjectDoesNotExist

from fb.storages.storage import StorageClass
import pytest


@pytest.mark.django_db
class TestReactToCommentExistsOrNot:

    def test_comment_reaction_exists_or_not_returns_react_dto(self,
                                                              react_to_comment_fixture):
        storage = StorageClass()
        reaction_dto = storage.comment_reaction_exists_or_not(
            react_to_comment_fixture.person_id,
            react_to_comment_fixture.id)
        assert reaction_dto.id == react_to_comment_fixture.id
        assert reaction_dto.reaction_type == react_to_comment_fixture.react_type
        assert reaction_dto.reacted_person_id == react_to_comment_fixture.person_id
        assert reaction_dto.comment_id == react_to_comment_fixture.comment_id

    def test_comment_reaction_exists_or_not_raises_exception(self):
        storage = StorageClass()
        with pytest.raises(ObjectDoesNotExist):
            storage.post_reaction_exists_or_not(1, 1)
