from fb.interactors.presenters.json_presenter import *


class Presenter(JsonPresenter):

    def create_post_response(self, post_id: int) -> dict:
        return {"id": post_id}

    def create_react_response(self, reaction_id: Optional[int]) -> dict:
        return {"id": reaction_id}

    def create_comment_response(self, comment_id: int) -> dict:
        return {"id": comment_id}

    def get_reactions_count_for_posts_response(self, count: int) -> dict:
        return {"count": count}

    def get_post_reacted_by_user_response(self, list_of_posts_id: List[int]) -> dict:
        posts_list = []
        for post_id in list_of_posts_id:
            posts_list.append({"id": post_id})
        return {"posts": posts_list}

    def get_positive_reacted_posts_response(self, list_positive_posts: List[int]) -> dict:
        posts_list = []
        for post_id in list_positive_posts:
            posts_list.append({"id": post_id})
        return {"posts": posts_list}

    def create_reactions_for_post_response(self, reactions_dto_list: List[
        ReactionsForPostDto]) -> dict:
        reactions_list = []
        for reaction_dto in reactions_dto_list:
            reactions_list.append(self.reactions_for_post_dto_to_dict(reaction_dto))
        return {"reactions": list}

    def reactions_for_post_dto_to_dict(self, reaction_for_post_dto):
        reaction_dict = {"username": reaction_for_post_dto.username,
                         "id": reaction_for_post_dto.id,
                         "profile_pic_url": reaction_for_post_dto.profile_url_pic,
                         "reaction_type": reaction_for_post_dto.reaction_type}
        return reaction_dict

    def get_post_metrics_response(self, post_metrics_dto_list: List[PostMetricsDto]) -> \
            dict:
        metrics_list = []
        for post_metrics_dto in post_metrics_dto_list:
            metrics_list.append({
                "type": post_metrics_dto.type,
                "count": post_metrics_dto.count
            })
        return {"reactions": metrics_list}

    def get_replies_for_comment_response(self, replies_dto_list: List[RepliesDto]) -> \
            dict:
        replies_list = []
        for reply_dto in replies_dto_list:
            replies_list.append(self.reply_dto_dict(reply_dto))
        return {"replies": replies_list}

    def reply_dto_dict(self, reply_dto):
        reply_dict = {}
        reply_person = reply_dto.commenter
        reply_dict['comment_id'] = reply_dto.comment_id
        reply_dict['commenter'] = {
            "username": reply_person.username,
            "id": reply_person.id,
            "profile_pic_url": reply_person.profile_url_pic
        }
        reply_dict['commented_at'] = reply_person.commented_at
        reply_dict['comment_content'] = reply_person.comment_content
        return reply_dict
