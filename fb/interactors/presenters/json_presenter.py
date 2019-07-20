import abc
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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
