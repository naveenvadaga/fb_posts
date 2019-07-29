import unittest
from fb.presenters.json_presenter import *


class TestPostMetrics(unittest.TestCase):

    def test_get_post_metrics(self):
        post_metrics_dto_1 = PostMetricsDto("haha", 2)
        post_metrics_dto_2 = PostMetricsDto("wow", 1)
        post_metrics_dto_3 = PostMetricsDto("like", 1)
        metrics_list = [post_metrics_dto_1, post_metrics_dto_2,
                        post_metrics_dto_3]

        json_presenter = JsonPresenter()
        response = json_presenter.get_post_metrics_response(metrics_list)
        response_reaction_metrics = response['reactions']
        test_metrics = {}
        for reaction_metric in response_reaction_metrics:
            if reaction_metric['type'] == post_metrics_dto_1.type:
                test_metrics = reaction_metric

        assert test_metrics['type'] == post_metrics_dto_1.type
        assert test_metrics['count'] == post_metrics_dto_1.count
