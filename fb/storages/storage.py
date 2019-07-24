from fb.interactors.storages.storage import *
from fb_post.models.models import *
from django.db.models import Count
from django.db.models import Q
from django.db.models import Prefetch


class StorageClass(Storage):

    def create_post(self, created_by_id: int, post_content: str) -> int:
        created_post = Post(person_id=created_by_id, post_content=post_content)
        created_post.save()
        return created_post.id

    def add_comment_to_post(self, post_id: int, commenter_id: int,
                            comment_text: str) -> int:
        created_comment = Comment(post_id=post_id, person_id=commenter_id,
                                  comment_content=comment_text)
        created_comment.save()
        return created_comment.id

    def parent_comment_id(self, comment_id) -> Optional[int]:
        reply_id = Comment.objects.get(id=comment_id).values_list('reply',
                                                                  flat=True)
        return reply_id

    def add_comment_to_comment(self, comment_id: int, commenter_id: int,
                               comment_text: str) -> int:
        created_comment = Comment(person_id=commenter_id,
                                  comment_text=comment_text,
                                  reply_id=comment_id)
        created_comment.save()
        return created_comment.id

    def delete_post(self, post_id: int) -> None:
        Post.objects.get(id=post_id).delete()

    def get_reactions_count_to_posts(self) -> int:
        return React.objects.exclude(post__isnull=True).count()

    def get_posts_reacted_by_user(self, user_id: int) -> List[int]:
        post_ids_list = React.objects.filter(person_id=user_id,
                                             comment_id__isnull=True). \
            values_list('post_id', flat=True)
        return post_ids_list

    def get_positive_reacted_posts(self) -> List[int]:
        reaction1 = Count('react',
                          filter=Q(react__react_type=ReactionChoice.Haha.value))
        reaction2 = Count('react',
                          filter=Q(react__react_type=ReactionChoice.Wow.value))
        reaction3 = Count('react',
                          filter=Q(react__react_type=ReactionChoice.Like.value))
        reaction4 = Count('react',
                          filter=Q(react__react_type=ReactionChoice.Love.value))
        reaction5 = Count('react', filter=Q(
            react__react_type=ReactionChoice.Angry.value))
        reaction6 = Count('react',
                          filter=Q(react__react_type=ReactionChoice.Sad.value))
        posts_id_list = Post.objects.annotate(
            positive=reaction1 + reaction2 + reaction3 + reaction4 - reaction5 - reaction6).filter(
            positive__gt=0 > 0).values_list('id', flat=True)
        return posts_id_list

    def get_post_reactions_metrics(self, post_id: int) -> List[PostMetricsDto]:
        metrics = []
        reactions_type_list_dict = React.objects.filter(post_id=post_id).values(
            'react_type').annotate(
            react_count=Count('react_type'))
        for d in reactions_type_list_dict:
            metrics.append(PostMetricsDto(d['react_type'], d['react_count']))
        return metrics

    def get_reactions_to_post(self, post_id: int, offset: int, limit: int) -> \
            List[ReactionsForPostDto]:
        reactions_to_posts_list = []
        reactions = React.objects.filter(post_id=post_id).select_related(
            'person')[offset:offset + limit]
        for reaction in reactions:
            reactions_to_posts_list.append(
                ReactionsForPostDto(reaction.person_id,
                                    reaction.person.username,
                                    reaction.person.profilePicUrl,
                                    reaction.react_type)
            )
        return reactions_to_posts_list

    def check_whether_given_id_is_comment_or_not(self, comment_id: int) -> None:
        from django.core.exceptions import SuspiciousOperation
        if Comment.objects.filter(id=comment_id,
                                  reply_id__isnull=False).exists():
            raise SuspiciousOperation
        return None

    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> \
            List[RepliesDto]:
        comments = Comment.objects.filter(reply_id=comment_id).select_related(
            'person')[offset: offset + limit]
        comments_replies_list = []
        for comment in comments:
            person_dto = PersonDto(comment.person.id, comment.person.username,
                                   comment.person.profilePicUrl)
            reply_dto = RepliesDto(comment.id, person_dto, comment.comment_at,
                                   comment.comment_content)
            comments_replies_list.append(reply_dto)
        return comments_replies_list

    def react_to_post_exists_or_not(self, reacted_person_id: int,
                                    post_id: int) -> ReactDto:
        reacted = React.objects.get(person_id=reacted_person_id,
                                    post_id=post_id)
        reaction_dto = ReactDto(reacted.id, reacted.react_type,
                                reacted.person_id, reacted.post_id,
                                reacted.comment_id)
        return reaction_dto

    def delete_reaction(self, reaction_id) -> None:
        React.objects.get(id=reaction_id).delete()

    def update_reaction_type(self, reaction_id: int, reaction_type: str) -> int:
        React.objects.filter(id=reaction_id).update(react_type=reaction_type)
        return reaction_id

    def react_to_comment(self, reacted_by_id: int, comment_id: int,
                         reaction_type: str) -> int:
        created_reaction = React(react_type=reaction_type,
                                 person_id=reacted_by_id, comment_id=comment_id)
        created_reaction.save()
        return created_reaction.id

    def react_to_comment_exists_or_not(self, reacted_person_id: int,
                                       comment_id: int) -> ReactDto:
        reacted_reaction = React.objects.get(person_id=reacted_person_id,
                                             comment_id=comment_id)
        reaction_dto = ReactDto(reacted_reaction.id,
                                reacted_reaction.react_type,
                                reacted_reaction.person_id,
                                reacted_reaction.post_id,
                                reacted_reaction.comment_id)
        return reaction_dto

    def react_to_post(self, reacted_by_id: int, post_id: int,
                      reaction_type: str) -> int:
        created_react = React(react_type=reaction_type, person_id=reacted_by_id,
                              post_id=post_id)
        created_react.save()
        return created_react.id

    def get_post_details(self, post_id: int) -> GetPostDto:
        post = Post.objects.select_related('person').get(id=post_id)
        reactions_to_post = React.objects.filter(post_id=post_id).values_list(
            'react_type', flat=True)
        comments_for_post = Comment.objects.filter(
            post_id=post_id).select_related('person').prefetch_related(
            Prefetch('comment_set', to_attr='replies'))
        comment_ids_list = []
        reply_ids_list = []
        for comment in comments_for_post:
            comment_ids_list.append(comment.id)
            for reply in comment.replies:
                reply_ids_list.append(reply.id)
        comment_reactions = React.objects.filter(
            comment_id__in=comment_ids_list).values('comment_id', 'react_type')
        reply_reactions = React.objects.filter(
            comment_id__in=reply_ids_list).values('comment_id', 'react_type')
        comment_reactions_dict = self.create_reactions_dict(comment_reactions)
        reply_reactions_dict = self.create_reactions_dict(reply_reactions)
        person_dto = PersonDto(post.person.id, post.person.username,
                               post.person.profilePicUrl)
        post_dto = PostDto(post.id, person_dto, post.post_content,
                           post.posted_at)
        reaction_type_dto_for_post = ReactionType(list(set(reactions_to_post)),
                                                  len(reactions_to_post))
        comments_list = self.comments_dto_list(comments_for_post,
                                               comment_reactions_dict,
                                               reply_reactions_dict)
        get_post_dto = GetPostDto(post_dto, reaction_type_dto_for_post,
                                  comments_list, len(comments_list))
        return get_post_dto

    def create_reactions_dict(self, reactions_dict_list):
        reactions_dict = {}
        for reaction in reactions_dict_list:
            if reaction['comment_id'] in reactions_dict:
                reactions_dict[reaction['comment_id']].add(
                    reaction['react_type'])
            else:
                reactions_dict[reaction['comment_id']] = {
                    reaction['react_type']}
        return reactions_dict

    def comments_dto_list(self, comments_for_post, comment_reactions_dict: dict,
                          reply_reactions_dict: dict) -> List[
        CommentForPostDetailsDto]:
        comments_list = []
        for comment in comments_for_post:
            post_comment_dto = self.create_post_comment_dto(comment,
                                                            comment_reactions_dict,
                                                            reply_reactions_dict)
            comments_list.append(post_comment_dto)
        return comments_list

    def create_post_comment_dto(self, comment, comment_reactions_dict,
                                reply_reactions_dict):
        comment_reaction_set = []
        comment_reaction_count = 0
        if comment.id in comment_reactions_dict:
            comment_reaction_count = len(comment_reactions_dict[comment.id])
            comment_reaction_set = list(comment_reactions_dict[comment.id])
        comment_reaction_type_dto = ReactionType(comment_reaction_set,
                                                 comment_reaction_count)
        comment_person_dto = PersonDto(comment.person.id,
                                       comment.person.username,
                                       comment.person.profilePicUrl)
        comment_dto = CommentDto(comment.id, comment_person_dto,
                                 comment.comment_at, comment.comment_content,
                                 comment_reaction_type_dto)
        replies_count = len(comment.replies)
        replies_list = self.replies_dto_list(comment.replies,
                                             comment_reactions_dict,
                                             reply_reactions_dict)
        post_comment_dto = CommentForPostDetailsDto(comment_dto, replies_count,
                                                    replies_list)
        return post_comment_dto

    def replies_dto_list(self, replies, comment_reactions_dict,
                         reply_reactions_dict):
        replies_list = []
        for reply in replies:
            reply_dto = self.create_reply_dto(reply, comment_reactions_dict,
                                              reply_reactions_dict)
            replies_list.append(reply_dto)
        return replies_list

    def create_reply_dto(self, reply, comment_reactions_dict,
                         reply_reactions_dict):
        reply_reaction_type = []
        reply_reaction_count = 0
        if reply.id in comment_reactions_dict:
            reply_reaction_count = len(reply_reactions_dict[reply.id])
            reply_reaction_type = list(reply_reactions_dict[reply.id])
        reply_reaction_dto = ReactionType(reply_reaction_type,
                                          reply_reaction_count)
        reply_person_dto = PersonDto(reply.person.id, reply.person.username,
                                     reply.person.profilePicUrl)
        reply_dto = CommentDto(reply.id, reply_person_dto, reply.comment_at,
                               reply.comment_content,
                               reply_reaction_dto)
        return reply_dto

    def get_posts_posted_by_person(self, person_id: int, offset: int,
                                   limit: int) -> List[GetPostDto]:
        posts_with_user_id = Post.objects.filter(person_id=person_id)[
                             offset:offset + limit].values('id')
        user_posts_list = []
        for post in posts_with_user_id:
            user_posts_list.append(self.get_post_details(post['id']))
        return user_posts_list
