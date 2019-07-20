import abc


class PostStorage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, created_by_id: int, post_content: str):
        pass
