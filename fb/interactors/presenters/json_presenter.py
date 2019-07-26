import abc
from typing import Optional, List
from ..storages.storage import PersonWithReactionDto, CommentDto, UserPostDto, \
    PostMetricsDto, CommentWithPersonDto


class JsonPresenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post_response(self, post_id: int) -> dict:
        pass

    @abc.abstractmethod
    def create_reaction_response(self, reaction_id: Optional[int]) -> dict:
        pass

    @abc.abstractmethod
    def create_comment_response(self, comment_id: int) -> dict:
        pass

    @abc.abstractmethod
    def create_post_reactions_response(self, reactions_list: List[
        PersonWithReactionDto]) -> dict:
        pass

    @abc.abstractmethod
    def get_post_reactions_count_response(self, count: int) -> dict:
        pass

    @abc.abstractmethod
    def get_user_reacted_posts_response(self, list_of_posts_id: List[int]) -> dict:
        pass

    @abc.abstractmethod
    def get_post_metrics_response(self, metrics: List[PostMetricsDto]) -> dict:
        pass

    @abc.abstractmethod
    def get_positive_reacted_posts_response(self, list_positive_posts: List[int]) -> dict:
        pass

    @abc.abstractmethod
    def get_comment_replies_response(self, replies: List[CommentWithPersonDto]) -> dict:
        pass

    @abc.abstractmethod
    def raise_invalid_comment_id(self) -> None:
        pass

    @abc.abstractmethod
    def get_post_details_response(self, get_post_dto: UserPostDto) -> dict:
        pass

    @abc.abstractmethod
    def raise_invalid_post_id(self) -> None:
        pass

    @abc.abstractmethod
    def delete_post_response(self) -> dict:
        pass

    @abc.abstractmethod
    def get_user_posts_response(self, list_of_posts: List[UserPostDto]) -> \
            List[dict]:
        pass
