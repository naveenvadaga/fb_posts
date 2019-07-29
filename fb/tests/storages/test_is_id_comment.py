from django.core.exceptions import SuspiciousOperation

from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestPostMetrics:

    def test_is_id_comment(self, comment_fixture):
        comment_id = comment_fixture.id
        storage = StorageImplementer()

        assert storage.is_id_comment(
            comment_id) is True

    def test_is_id_comment_when_id_is_reply(self, reply_fixture):
        reply_id = reply_fixture.id
        storage = StorageImplementer()

        assert storage.is_id_comment(reply_id) is False
