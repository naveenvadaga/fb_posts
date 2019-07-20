import abc
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostDto:
    id: int
    posted_person: int
    post_content: str
    posted_at: datetime


class PostPresenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post_response(self, post: PostDto):
        pass
