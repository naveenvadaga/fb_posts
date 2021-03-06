import unittest
from unittest.mock import Mock

from fb.interactors.storages.storage import Storage, PostMetricsDto
from fb.interactors.presenters.presenter import Presenter
from fb.interactors.post_interactor import PostInteractor
from dataclasses import fields


class TestGetPostMetrics(unittest.TestCase):

    def test_get_post_metrics_returns_reaction_metrics(self):
        mock_storage = Mock(spec=Storage)
        mock_json_presenter = Mock(spec=Presenter)
        post_id = 1
        post_metrics_haha_dto = Mock(
            spec=[field.name for field in fields(PostMetricsDto)])
        post_metrics_wow_dto = Mock(
            sspec=[field.name for field in fields(PostMetricsDto)])
        post_metrics_sad_dto = Mock(
            spec=[field.name for field in fields(PostMetricsDto)])
        post_metrics = [post_metrics_haha_dto, post_metrics_sad_dto,
                        post_metrics_wow_dto]

        mock_response = {'reactions': post_metrics}

        mock_storage.get_post_metrics.return_value = post_metrics
        mock_json_presenter.get_post_metrics_response.return_value = mock_response

        post_interactor = PostInteractor(mock_json_presenter, mock_storage)
        response_from_get_post_metrics = post_interactor. \
            get_post_metrics(post_id)

        mock_storage.get_post_metrics.assert_called_once_with(post_id)
        mock_json_presenter.get_post_metrics_response.assert_called_once_with(
            post_metrics)
        assert response_from_get_post_metrics == mock_response
