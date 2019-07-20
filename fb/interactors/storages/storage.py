import abc
from datetime import datetime
from typing import Optional
from dataclasses import dataclass


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


class Storage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, created_by_id: int, post_content: str) -> int:
        pass

    @abc.abstractmethod
    def add_comment(self, post_id: int, commenter_id: int, comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def reply_to_comment(self, comment_id: int, commenter_id: int, comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def react_to_post_exists(self, reacted_person_id: int, post_id: int) -> int:
        pass

    @abc.abstractmethod
    def react_to_comment_exits(self, reacted_person_id: int, comment_id: int) -> int:
        pass

    @abc.abstractmethod
    def get_reaction_type_for_reaction(self, reaction_id: int) -> str:
        pass

    @abc.abstractmethod
    def update_reaction_type(self, reaction_id: int, reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def delete_reaction(self, reaction_id) -> None:
        pass

    @abc.abstractmethod
    def react_to_post(self, reacted_by_id: int, post_id: int, reaction_type: str) -> Optional[int]:
        pass

    @abc.abstractmethod
    def react_to_comment(self, reacted_by_id: int, comment_id: int, reaction_type: str) -> Optional[int]:
        pass
