import abc
from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class PersonDto:
    id: int
    username: str
    profile_url_pic: str


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


@dataclass
class ReactionsForPostDto(PersonDto):
    reaction_type: str


class Storage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, created_by_id: int, post_content: str) -> int:
        pass

    @abc.abstractmethod
    def add_comment_to_post(self, post_id: int, commenter_id: int, comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def add_comment_to_comment(self, comment_id: int, commenter_id: int, comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def comment_reply_id_field(self, comment_id) -> Optional[int]:
        pass

    @abc.abstractmethod
    def react_to_post_exists(self, reacted_person_id: int, post_id: int) -> ReactDto:
        pass

    @abc.abstractmethod
    def react_to_comment_exits(self, reacted_person_id: int, comment_id: int) -> ReactDto:
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

    @abc.abstractmethod
    def get_reactions_to_post(self, post_id: int, offset: int, limit: int) -> List[ReactionsForPostDto]:
        pass

    @abc.abstractmethod
    def get_reactions_count_to_posts(self) -> int:
        pass

    @abc.abstractmethod
    def get_post_reacted_by_user(self, user_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def get_post_metrics(self, post_id: int) -> dict:
        pass

    @abc.abstractmethod
    def get_positive_reacted_posts(self) -> List[int]:
        pass
