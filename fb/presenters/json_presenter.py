from fb.interactors.presenters.presenter import *
from fb.interactors.storages.storage import CommentWithPersonDto, PersonDto, \
    ReactionDto, PostDto


class JsonPresenter(Presenter):

    def create_post_response(self, post_id: int) -> dict:

        return {"id": post_id}

    def create_reaction_response(self, reaction_id: Optional[int]) -> dict:

        return {"id": reaction_id}

    def create_comment_response(self, comment_id: int) -> dict:

        return {"id": comment_id}

    def get_post_reactions_count_response(self, count: int) -> dict:

        return {"count": count}

    def get_user_reacted_posts_response(self,
                                        post_dto_list_id: List[int]) -> dict:
        post_ids_list = []

        for post_id in post_dto_list_id:
            post_ids_list.append({"id": post_id})

        return {"posts": post_ids_list}

    def get_more_positive_reacted_posts_response(self, positive_post_ids_list:
    List[int]) -> dict:

        posts_list = []

        for post_id in positive_post_ids_list:
            posts_list.append({"id": post_id})

        return {"posts": posts_list}

    def create_post_reactions_response(self, reaction_dtos_list: List[
        PersonWithReactionDto]) -> dict:

        reactions_list = []

        for reaction_dto in reaction_dtos_list:
            reactions_list.append(self.get_reaction_detail_dict(reaction_dto))

        return {"reactions": reactions_list}

    def get_reaction_detail_dict(self, post_reaction_dto):

        reaction_dto = post_reaction_dto.reaction

        reaction_dict = {"username": post_reaction_dto.username,
                         "id": post_reaction_dto.id,
                         "profile_pic_url": post_reaction_dto.profile_url_pic,
                         "reaction_type": reaction_dto.reaction_type}

        return reaction_dict

    def get_post_metrics_response(self, post_metrics_dto_list: List[
        PostMetricsDto]) -> dict:

        metrics_list = []

        for post_metrics_dto in post_metrics_dto_list:
            metrics_list.append({
                "type": post_metrics_dto.type,
                "count": post_metrics_dto.count
            })

        return {"reactions": metrics_list}

    def get_comment_replies_response(self, replies_dto_list: List[
        CommentWithPersonDto]) -> dict:

        replies_list = []

        for reply_dto in replies_dto_list:
            replies_list.append(self.get_reply_dict(reply_dto))

        return {"replies": replies_list}

    def get_reply_dict(self, comment_with_person_dto):

        comment_dto = comment_with_person_dto.comment
        person_dto = comment_with_person_dto.person

        commenter_dict = {
            "username": person_dto.username,
            "id": person_dto.id,
            "profile_pic_url": person_dto.profile_url_pic
        }

        return {
            "comment_id": comment_dto.comment_id,
            "commenter": commenter_dict,
            "commented_at": comment_dto.commented_at,
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

        comment_wise_reactions_stats_dict = \
            self.get_comment_wise_reaction_stats_dict(
                get_post_dto.reactions)

        person_dto_list = get_post_dto.persons
        comment_dto_list = get_post_dto.comments

        person_wise_dict = self.get_person_wise_dict(person_dto_list)
        comment_wise_dict = \
            self.get_comment_wise_dict(comment_dto_list,
                                       person_wise_dict,
                                       comment_wise_reactions_stats_dict)
        comment_wise_details_list = self.get_comment_wise_details_list(
            comment_dto_list, comment_wise_dict)

        get_post_dict = {"post_id": post_dto.id,
                         "posted_by": person_wise_dict[
                             post_dto.posted_person_id],
                         "posted_at": self.get_formatted_date_time(
                             post_dto.posted_at),
                         "post_content": post_dto.post_content,
                         "reactions": self.get_post_reaction_stats_dict(
                             post_dto.id,
                             get_post_dto.reactions),
                         "comments": comment_wise_details_list,
                         "comments_count": len(comment_wise_details_list)}
        return get_post_dict

    def get_person_wise_dict(self, person_dto_list):

        person_wise_dict = {}

        for person_dto in person_dto_list:
            person_wise_dict[person_dto.id] = {
                "username": person_dto.username,
                "id": person_dto.id,
                "profile_pic_url": person_dto.profile_url_pic
            }

        return person_wise_dict

    def get_comment_wise_dict(self, comment_dto_list, person_wise_dict,
                              comment_wise_reactions_stats_dict):

        comment_wise_dict = {}

        for comment_dto in comment_dto_list:
            comment_dict = self.get_comment_with_reactions_dict(
                comment_dto, person_wise_dict,
                comment_wise_reactions_stats_dict)

            comment_wise_dict[comment_dto.comment_id] = comment_dict

        return comment_wise_dict

    def get_comment_with_reactions_dict(self, comment_dto, person_wise_dict,
                                        comment_wise_reactions_stats_dict):

        comment_dict = {
            "comment_id": comment_dto.comment_id,
            "commenter": person_wise_dict[comment_dto.commenter_id],
            "commented_at": self.get_formatted_date_time(
                comment_dto.commented_at),
            "comment_content": comment_dto.comment_content
        }

        if comment_dto.comment_id in comment_wise_reactions_stats_dict:
            comment_dict["reactions"] = comment_wise_reactions_stats_dict[
                comment_dto.comment_id]
        else:
            comment_dict["reactions"] = {
                "count": 0,
                "type": []
            }

        return comment_dict

    def get_post_reaction_stats_dict(self, post_id, reaction_dto_list):

        reaction_types = []

        for reaction_dto in reaction_dto_list:
            if reaction_dto.post_id == post_id:
                reaction_types.append(reaction_dto.reaction_type)

        reaction_types_count = len(reaction_types)

        return {
            "type": reaction_types,
            "count": reaction_types_count
        }

    def get_comment_wise_reaction_stats_dict(self, reaction_dto_list):

        reaction_stats_dict = {}

        for reaction_dto in reaction_dto_list:
            try:
                reaction_stats_dict[reaction_dto.comment_id]["count"] += 1
                reaction_stats_dict[reaction_dto.comment_id]["type"].append(
                    reaction_dto.reaction_type)
            except KeyError:
                reaction_stats_dict[reaction_dto.comment_id] = {
                    "count": 1, "type": [reaction_dto.reaction_type]}

        return reaction_stats_dict

    def get_comment_wise_details_list(self, comment_dto_list,
                                      comment_wise_dict):

        comment_list = []

        for comment_dto in comment_dto_list:
            if comment_dto.post_id != 0:
                replies = self.get_comment_wise_reply_list(
                    comment_dto.comment_id, comment_dto_list,
                    comment_wise_dict)
                dict = {**comment_wise_dict[comment_dto.comment_id],
                        "replies_count": len(replies),
                        "replies": replies}
                comment_list.append(dict)

        return comment_list

    def get_comment_wise_reply_list(self, comment_id, comments_dto_list,
                                    comment_wise_dict):

        reply_list = []

        for comment_dto in comments_dto_list:
            if comment_dto.commented_on_id == comment_id:
                reply_list.append(comment_wise_dict[comment_dto.comment_id])

        return reply_list

    def get_formatted_date_time(self, date_time):

        return date_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_user_posts_response(self, post_dto_list: List[UserPostDto]) -> \
            List[dict]:
        get_post_details_list = []

        for get_post_details_dto in post_dto_list:
            get_post_details_list.append(
                self.get_post_details_response(get_post_details_dto))

        return get_post_details_list

    def delete_post_response(self) -> dict:
        return {}
