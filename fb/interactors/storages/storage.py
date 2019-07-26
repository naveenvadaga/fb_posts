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
    posted_person_id: int
    post_content: str
    posted_at: datetime


@dataclass
class ReactionDto:
    reaction_type: str
    id: int = 0
    reacted_person_id: int = 0
    post_id: int = 0
    comment_id: int = 0


@dataclass
class PersonWithReactionDto(PersonDto):
    reaction: ReactionDto


@dataclass
class PostMetricsDto:
    type: str
    count: int


@dataclass
class CommentDto:
    comment_id: int
    commenter_id: int
    commented_at: datetime
    comment_content: str
    post_id: int = 0
    commented_on_id: int = 0


@dataclass
class CommentWithPersonDto:
    comment: CommentDto
    person: PersonDto


@dataclass
class UserPostDto:
    post: PostDto
    persons: List[PersonDto]
    reactions: List[ReactionDto]
    comments: List[CommentDto]


class Storage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, created_by_id: int, post_content: str) -> int:
        pass

    @abc.abstractmethod
    def add_comment_to_post(self, post_id: int, commenter_id: int,
                            comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def add_reply_to_comment(self, comment_id: int, commenter_id: int,
                             comment_text: str) -> int:
        pass

    @abc.abstractmethod
    def get_parent_comment_id(self, comment_id) -> Optional[int]:
        pass

    @abc.abstractmethod
    def get_post_reaction(self, reacted_person_id: int,
                          post_id: int) -> ReactionDto:
        pass

    @abc.abstractmethod
    def get_comment_reaction(self, reacted_person_id: int,
                             comment_id: int) -> ReactionDto:
        pass

    @abc.abstractmethod
    def update_reaction(self, reaction_id: int, reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def delete_reaction(self, reaction_id) -> None:
        pass

    @abc.abstractmethod
    def react_to_post(self, reacted_by_id: int, post_id: int, reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def react_to_comment(self, reacted_by_id: int, comment_id: int,
                         reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def get_post_reactions(self, post_id: int, offset: int, limit: int) -> List[
         PersonWithReactionDto]:
        pass

    @abc.abstractmethod
    def get_total_post_reactions_count(self) -> int:
        pass

    @abc.abstractmethod
    def get_user_reacted_post_ids(self, user_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def get_post_reaction_metrics(self, post_id: int) -> List[PostMetricsDto]:
        pass

    @abc.abstractmethod
    def get_more_positive_reacted_post_ids(self) -> List[int]:
        pass

    @abc.abstractmethod
    def is_id_comment(self, comment_id: int) -> None:
        pass

    @abc.abstractmethod
    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> List[
         CommentWithPersonDto]:
        pass

    @abc.abstractmethod
    def get_post_details(self, post_id: int) -> UserPostDto:
        pass

    @abc.abstractmethod
    def delete_post(self, post_id: int) -> None:
        pass

    @abc.abstractmethod
    def get_user_posts(self, person_id: int, offset: int, limit: int) -> List[
         UserPostDto]:
        pass
