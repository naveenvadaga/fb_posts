from fb.interactors.presenters.json_presenter import *
from fb.interactors.storages.storage import CommentWithPersonDto


class Presenter(JsonPresenter):

    def create_post_response(self, post_id: int) -> dict:
        return {"id": post_id}

    def create_reaction_response(self, reaction_id: Optional[int]) -> dict:
        return {"id": reaction_id}

    def create_comment_response(self, comment_id: int) -> dict:
        return {"id": comment_id}

    def get_posts_reactions_count_response(self, count: int) -> dict:
        return {"count": count}

    def get_user_reacted_posts_response(self, list_of_posts_id: List[int]) -> dict:
        posts_id_list = []
        for post_id in list_of_posts_id:
            posts_id_list.append({"id": post_id})
        return {"posts": posts_id_list}

    def get_positive_reacted_posts_response(self, list_positive_posts: List[int]) -> dict:
        posts_list = []
        for post_id in list_positive_posts:
            posts_list.append({"id": post_id})
        return {"posts": posts_list}

    def create_post_reactions_response(self, reactions_dto_list: List[
        PersonWithReactionDto]) -> dict:
        reactions_list = []
        for reaction_dto in reactions_dto_list:
            reactions_list.append(self.get_reactions_detail_dict(reaction_dto))
        return {"reactions": list}

    def get_reactions_detail_dict(self, reaction_for_post_dto):
        reaction_dto = reaction_for_post_dto.reaction
        reaction_dict = {"username": reaction_for_post_dto.username,
                         "id": reaction_for_post_dto.id,
                         "profile_pic_url": reaction_for_post_dto.profile_url_pic,
                         "reaction_type": reaction_dto.react_type}
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

    def get_comment_replies_response(self, replies_dto_list: List[CommentWithPersonDto]) -> \
            dict:
        replies_list = []
        for reply_dto in replies_dto_list:
            replies_list.append(self.get_reply_dict(reply_dto))
        return {"replies": replies_list}

    def get_reply_dict(self, comment_with_person_dto):
        comment_dto = comment_with_person_dto.comment
        person_dto = comment_with_person_dto.person
        commenter_dict = {
            "name": person_dto.username,
            "user_id": person_dto.id,
            "profile_pic_url": person_dto.profile_url_pic
        }
        return {
            "comment_id": comment_dto.id,
            "commenter": commenter_dict,
            "commented_at": comment_dto.comment_at,
            "comment_content": comment_dto.comment_content
        }

    def raise_invalid_comment_id(self) -> None:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid comment id', 'INVALID_COMMENT_ID')

    def raise_invalid_post_id(self) -> None:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')

    def get_post_details_response(self, get_post_dto: UserPostDto) -> dict:
        post_dto = get_post_dto.post
        comments_reactions_dict = self.get_comments_reactions_stats_dict(
            get_post_dto.reactions)
        person_dto_list = get_post_dto.persons
        comments_dto = get_post_dto.comments
        persons_dict = self.get_persons_dict(person_dto_list)
        comments_dict = self.get_comments_dict(comments_dto, persons_dict, comments_reactions_dict)
        comments_list = self.get_comment_details_dict(comments_dto, comments_dict)
        get_post_dict = {}
        get_post_dict["post_id"] = post_dto.id
        get_post_dict["posted_by"] = persons_dict[post_dto.posted_person_id]
        get_post_dict["posted_at"] = post_dto.posted_at.strftime("%Y-%m-%d, %H:%M:%S")
        get_post_dict["post_content"] = post_dto.post_content
        get_post_dict["reactions"] = self.get_post_reactions_stats_dict(post_dto.id,
                                                                        get_post_dto.reactions)
        get_post_dict["comments"] = comments_list
        get_post_dict["comments_count"] = len(comments_list)
        return get_post_dict

    def get_persons_dict(self, person_dto_list):
        persons_dict = {}
        for person_dto in person_dto_list:
            persons_dict[person_dto.id] = {
                "name": person_dto.username,
                "user_id": person_dto.id,
                "profile_pic_url": person_dto.profile_url_pic
            }
        return persons_dict

    def get_person_dict(self, person_id, person_dto_list):
        for person_dto in person_dto_list:
            if person_dto.id == person_id:
                return {
                    "name": person_dto.username,
                    "user_id": person_dto.id,
                    "profile_pic_url": person_dto.profile_url_pic
                }

    def get_post_reactions_stats_dict(self, post_id, reaction_dto_list):
        reactions_types = []
        for reaction in reaction_dto_list:
            if reaction.post == post_id:
                reactions_types.append(reaction.react_type)
        reactions_types_count = len(reactions_types)
        return {
            "type": reactions_types,
            "count": reactions_types_count
        }

    def get_comments_reactions_stats_dict(self, reaction_dto_list):
        reactions_stats_dict = {}
        for reaction in reaction_dto_list:
            try:
                reactions_stats_dict[reaction.comment]["count"] = reactions_stats_dict[
                                                                      reaction.comment][
                                                                      "count"] + 1
                reactions_stats_dict[reaction.comment]["type"].append(reaction.react_type)
            except Exception:
                reactions_stats_dict[reaction.comment] = {
                    "count": 1,
                    "type": [reaction.react_type]
                }
        return reactions_stats_dict

    def get_comment_details_dict(self, comments, comments_dict):
        comments_list = []
        for comment in comments:
            if comment.post != 0:
                replies = self.get_replies_for_comment_dict(comment.comment_id, comments, comments_dict)
                dict = {**comments_dict[comment.comment_id],
                        "replies_count": len(replies),
                        "replies": replies}
                comments_list.append(dict)
        return comments_list

    def get_replies_for_comment_dict(self, comment_id, comments, comments_dict):
        replies_list = []
        for comment in comments:
            if comment.reply == comment_id:
                replies_list.append(comments_dict[comment.comment_id])
        return replies_list

    def get_comments_dict(self, comments_dto, persons_dict, comments_reactions_dict):
        comments_dict = {}
        for comment in comments_dto:
            comment_dict = self.get_comment_dict(comment, persons_dict, comments_reactions_dict)
            comments_dict[comment.comment_id] = comment_dict
        return comments_dict

    def get_comment_dict(self, comment, persons_dict, comments_reactions_dict):
        comment_dict = {}
        comment_dict["comment_id"] = comment.comment_id
        comment_dict["commenter"] = persons_dict[comment.commenter_id]
        comment_dict["commented_at"] = comment.commented_at.strftime("%m/%d/%Y, %H:%M:%S")
        comment_dict["comment_content"] = comment.comment_content
        if comment.comment_id in comments_reactions_dict:
            comment_dict["reactions"] = comments_reactions_dict[comment.comment_id]
        else:
            comment_dict["reactions"] = {
                "count": 0,
                "type": []
            }
        return comment_dict

    def get_user_posts_response(self, list_of_posts: List[UserPostDto]) -> \
            List[dict]:
        get_post_details_list = []
        for get_post_details_dto in list_of_posts:
            get_post_details_list.append(
                self.get_post_details_response(get_post_details_dto))
        return get_post_details_list

    def delete_post_response(self) -> dict:
        return {}
