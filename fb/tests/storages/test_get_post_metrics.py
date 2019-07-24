from fb.storages.storage import *
import pytest


@pytest.mark.django_db
class TestGetPostMetrics:

    @pytest.fixture()
    def metrics_setup(self, post_fixture, persons_fixture):
        self.post_id = post_fixture.id
        self.react_type1 = "haha"
        self.react_type2 = "wow"
        self.react_type3 = "like"
        self.react_type4 = "sad"
        person1 = persons_fixture[0]
        person2 = persons_fixture[1]
        person3 = persons_fixture[2]
        person4 = persons_fixture[3]
        person5 = persons_fixture[4]
        React(person=person1, post_id=self.post_id,
              react_type=self.react_type1).save()
        React(person=person2, post_id=self.post_id,
              react_type=self.react_type2).save()
        React(person=person3, post_id=self.post_id,
              react_type=self.react_type1).save()
        React(person=person4, post_id=self.post_id,
              react_type=self.react_type3).save()
        React(person=person5, post_id=self.post_id,
              react_type=self.react_type4).save()

    def test_get_post_metrics_returns_metrics(self, metrics_setup):
        storage = StorageClass()
        reaction_metrics = storage.get_post_metrics(self.post_id)
        dict = {}
        for dto in reaction_metrics:
            dict[dto.type] = dto.count
        assert len(reaction_metrics) == 4
        assert dict[self.react_type1] == 2
        assert dict[self.react_type2] == 1
        assert dict[self.react_type3] == 1
        assert dict[self.react_type4] == 1

    def test_get_post_metrics_returns_empty_metrics(self, post_fixture):
        post_id = post_fixture.id
        storage = StorageClass()
        reaction_metrics = storage.get_post_metrics(post_id)
        assert len(reaction_metrics) == 0
