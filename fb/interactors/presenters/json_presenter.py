import abc
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from ..storages.storage import ReactionsForPostDto


@dataclass
class PostDto:
    id: int
    posted_person: int
    post_content: str
    posted_at: datetime


@dataclass
class ReactDto:
    id: int
    react_type: str
    reacted_person: int
    post: Optional[int]
    comment: Optional[int]


class JsonPresenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post_response(self, post_id: int) -> dict:
        pass

    @abc.abstractmethod
    def create_react_response(self, reaction_id: Optional[int]) -> dict:
        pass

    @abc.abstractmethod
    def create_comment_response(self, comment_id: int) -> dict:
        pass

    @abc.abstractmethod
    def create_reactions_for_post_response(self, reactions_list: List[ReactionsForPostDto]) -> dict:
        pass

    @abc.abstractmethod
    def get_reactions_count_for_posts_response(self, count: int) -> dict:
        pass

    @abc.abstractmethod
    def get_post_reacted_by_user_response(self, list_of_posts_id: List[int]) -> dict:
        pass

    @abc.abstractmethod
    def get_post_metrics_response(self, metrics: dict) -> dict:
        pass

    @abc.abstractmethod
    def get_positive_reacted_posts_response(self, list_positive_posts: List[int]) -> dict:
        pass
