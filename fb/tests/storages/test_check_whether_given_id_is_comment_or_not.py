from django.core.exceptions import SuspiciousOperation

from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestPostMetrics:

    def test_when_comment_is_not_reply(self, comment_fixture):
        comment_id = comment_fixture.id
        storage = StorageClass()
        assert storage.is_id_comment(
            comment_id) is None

    def test_when_comment_is_reply(self, reply_fixture):
        reply_id = reply_fixture.id
        storage = StorageClass()
        with pytest.raises(SuspiciousOperation):
            storage.is_id_comment(reply_id)
