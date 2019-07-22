# from typing import Optional, List
from fb.interactors.storages.storage import *
from fb.models.models import *
from django.db.models import Count
from django.db.models import Q


class StorageClass(Storage):

    def create_post(self, created_by_id: int, post_content: str) -> int:
        post_created = Post(person=created_by_id, post_content=post_content)
        post_created.save()
        return post_created.id

    def add_comment_to_post(self, post_id: int, commenter_id: int, comment_text: str) -> int:
        comment_created = Comment(post=post_id, person=commenter_id, comment_content=comment_text)
        comment_created.save()
        return comment_created.id

    def comment_reply_id_field(self, comment_id) -> Optional[int]:
        reply_id = Comment.objects.filter(id=comment_id).values_list('reply', flat=True)[0]
        return reply_id

    def add_comment_to_comment(self, comment_id: int, commenter_id: int, comment_text: str) -> int:
        comment_created = Comment(person=commenter_id, comment_text=comment_text, reply=comment_id)
        return comment_created.id

    def delete_post(self, post_id: int) -> None:
        Post.objects.get(id=post_id).delete()

    def get_reactions_count_to_posts(self) -> int:
        return React.objects.exclude(post__isnull=True).count()

    def get_post_reacted_by_user(self, user_id: int) -> List[int]:
        post_ids = React.objects.filter(person=user_id).values_list('post_id', flat=True)
        return post_ids

    def get_positive_reacted_posts(self) -> List[int]:
        reaction1 = Count('react', filter=Q(react__react_type=ReactionChoice.Haha.value))
        reaction2 = Count('react', filter=Q(react__react_type=ReactionChoice.Wow.value))
        reaction3 = Count('react', filter=Q(react__react_type=ReactionChoice.Like.value))
        reaction4 = Count('react', filter=Q(react__react_type=ReactionChoice.Love.value))
        reaction5 = Count('react', filter=Q(react__react_type=ReactionChoice.Angry.value))
        reaction6 = Count('react', filter=Q(react__react_type=ReactionChoice.Sad.value))
        posts_id_list = Post.objects.annotate(
            positive=reaction1 + reaction2 + reaction3 + reaction4 - reaction5 - reaction6).filter(
            positive__gt=0 > 0).values_list('id', flat=True)
        return posts_id_list

    def get_post_metrics(self, post_id: int) -> List[PostMetricsDto]:
        metrics = []
        dict = React.objects.filter(post_id=post_id).values('react_type').annotate(react_count=Count('react_type'))
        for d in dict:
            metrics.append(PostMetricsDto(d['react_type'], d['react_count']))
        return metrics

    def get_reactions_to_post(self, post_id: int, offset: int, limit: int) -> List[ReactionsForPostDto]:
        reactions_to_posts = []
        reactions = React.objects.filter(post_id=post_id).select_related('person')[offset:offset + limit]
        for reaction in reactions:
            reactions_to_posts.append(
                ReactionsForPostDto(reaction.person_id, reaction.person.username, reaction.person.profilePicUrl,
                                    reaction.react_type)
            )
        return reactions_to_posts

    def get_comment_with_comment_id_and_reply(self, comment_id: int) -> None:
        from django.core.exceptions import SuspiciousOperation
        if Comment.objects.filter(id=comment_id, reply_id__isnull=False).count() > 0:
            raise SuspiciousOperation

    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> List[RepliesDto]:
        comments = Comment.objects.filter(reply_id=comment_id).select_related('person')[offset: offset + limit]
        comments_replies_list = []
        for comment in comments:
            person_dto = PersonDto(comment.person.id, comment.person.username, comment.person.profilePicUrl)
            reply_dto = RepliesDto(comment.id, person_dto, comment.comment_at, comment.comment_content)
            comments_replies_list.append(reply_dto)
        return comments_replies_list

    def react_to_post_exists(self, reacted_person_id: int, post_id: int) -> ReactDto:
        reacted = React.objects.get(person_id=reacted_person_id, post_id=post_id)
        reaction_dto = ReactDto(reacted.id, reacted.react_type, reacted.person_id, reacted.post_id, reacted.comment_id)
        return reaction_dto

    def delete_reaction(self, reaction_id) -> None:
        React.objects.get(id=reaction_id).delete()

    def update_reaction_type(self, reaction_id: int, reaction_type: str) -> int:
        React.objects.get(id=reaction_id).update(react_type=reaction_type)
        return reaction_id

    def react_to_comment(self, reacted_by_id: int, comment_id: int, reaction_type: str) -> int:
        react_created = React(react_type=reaction_type, person=reacted_by_id, comment_id=comment_id)
        react_created.save()
        return react_created.id

    def react_to_comment_exists(self, reacted_person_id: int, comment_id: int) -> ReactDto:
        reacted = React.objects.get(person_id=reacted_person_id, comment_id=comment_id)
        reaction_dto = ReactDto(reacted.id, reacted.react_type, reacted.person_id, reacted.post_id, reacted.comment_id)
        return reaction_dto

    def react_to_post(self, reacted_by_id: int, post_id: int, reaction_type: str) -> int:
        react_created = React(react_type=reaction_type, person=reacted_by_id, post_id=post_id)
        react_created.save()
        return react_created.id

    def get_post_details(self, post_id: int) -> GetPostDto:
        pass

    def get_posts_posted_by_person(self, person_id: int) -> List[GetPostDto]:
        pass
