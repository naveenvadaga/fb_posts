from fb.interactors.storages.storage import *
from fb_post.models.models import *
from django.db.models import Count
from django.db.models import Q
from django.db.models import Prefetch


class StorageImplementer(Storage):

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

    def get_parent_comment_id(self, comment_id) -> Optional[int]:

        reply_id = Comment.objects.get(id=comment_id).reply_id

        return reply_id

    def add_reply_to_comment(self, comment_id: int, commenter_id: int,
                             comment_text: str) -> int:
        created_comment = Comment(person_id=commenter_id,
                                  comment_content=comment_text,
                                  reply_id=comment_id)
        created_comment.save()
        return created_comment.id

    def delete_post(self, post_id: int) -> None:

        Post.objects.get(id=post_id).delete()

    def get_total_post_reactions_count(self) -> int:
        return Reaction.objects.exclude(post__isnull=True).count()

    def get_user_reacted_post_ids(self, user_id: int) -> List[int]:
        post_ids_list = Reaction.objects.filter(person_id=user_id,
                                                comment_id__isnull=True). \
            values_list('post_id', flat=True)
        return post_ids_list

    def get_more_positive_reacted_post_ids(self) -> List[int]:

        positive_values_list = [ReactionChoice.Haha.value,
                                ReactionChoice.Like.value,
                                ReactionChoice.Wow.value,
                                ReactionChoice.Love.value
                                ]

        negative_values_list = [ReactionChoice.Sad.value,
                                ReactionChoice.Angry.value]

        positive_reaction = Count(
            'reaction',
            filter=Q(reaction__react_type__in=positive_values_list))
        negative_reaction = Count(
            'reaction',
            filter=Q(reaction__react_type__in=negative_values_list))

        post_ids_list = Post.objects.annotate(
            positive=positive_reaction - negative_reaction).filter(
            positive__gt=0 > 0).values_list('id', flat=True)

        return post_ids_list

    def get_post_reaction_metrics(self, post_id: int) -> List[PostMetricsDto]:
        metrics = []

        reactions_type_list_dict = Reaction.objects.filter(
            post_id=post_id).values(
            'react_type').annotate(
            react_count=Count('react_type'))

        for reaction_type in reactions_type_list_dict:
            metrics.append(PostMetricsDto(reaction_type['react_type'],
                                          reaction_type['react_count']))

        return metrics

    def get_post_reactions(self, post_id: int, offset: int, limit: int) -> \
            List[PersonWithReactionDto]:

        reactions_to_post_list = []

        reactions = Reaction.objects.filter(post_id=post_id).select_related(
            'person')[offset:offset + limit]

        for reaction in reactions:
            reaction_dto = ReactionDto(reaction.react_type, reaction.id,
                                       reaction.person)
            reactions_to_post_list.append(
                PersonWithReactionDto(reaction.person_id,
                                      reaction.person.username,
                                      reaction.person.profilePicUrl,
                                      reaction_dto))

        return reactions_to_post_list

    def is_id_comment(self, comment_id: int) -> bool:

        if Comment.objects.filter(id=comment_id,
                                  reply_id__isnull=False).exists():
            return False

        return True

    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> \
            List[CommentWithPersonDto]:

        comments = Comment.objects.filter(reply_id=comment_id).select_related(
            'person')[offset: offset + limit]

        comment_replies_list = []

        for comment in comments:
            person_dto = PersonDto(comment.person.id, comment.person.username,
                                   comment.person.profilePicUrl)
            comment_dto = CommentDto(comment.id, comment.person.id,
                                     comment.comment_at,
                                     comment.comment_content)
            comment_with_person_dto = CommentWithPersonDto(comment_dto,
                                                           person_dto)
            comment_replies_list.append(comment_with_person_dto)

        return comment_replies_list

    def get_post_reaction(self, reacted_person_id: int,
                          post_id: int) -> ReactionDto:

        reaction = Reaction.objects.get(person_id=reacted_person_id,
                                       post_id=post_id)

        reaction_dto = ReactionDto(reaction.react_type, reaction.id,
                                   reaction.person_id, reaction.post_id,
                                   reaction.comment_id)

        return reaction_dto

    def delete_reaction(self, reaction_id) -> None:

        Reaction.objects.get(id=reaction_id).delete()

    def update_reaction(self, reaction_id: int, reaction_type: str) -> int:

        Reaction.objects.filter(id=reaction_id).update(
            react_type=reaction_type)

        return reaction_id

    def react_to_comment(self, reacted_by_id: int, comment_id: int,
                         reaction_type: str) -> int:

        created_reaction = Reaction(react_type=reaction_type,
                                    person_id=reacted_by_id,
                                    comment_id=comment_id)

        created_reaction.save()

        return created_reaction.id

    def get_comment_reaction(self, reacted_person_id: int,
                             comment_id: int) -> ReactionDto:

        reaction = Reaction.objects.get(person_id=reacted_person_id,
                                                comment_id=comment_id)

        reaction_dto = ReactionDto(reaction.react_type,
                                   reaction.id,
                                   reaction.person_id,
                                   reaction.post_id,
                                   reaction.comment_id)

        return reaction_dto

    def react_to_post(self, reacted_by_id: int, post_id: int,
                      reaction_type: str) -> int:
        reaction = Reaction(react_type=reaction_type,
                                 person_id=reacted_by_id,
                                 post_id=post_id)

        reaction.save()
        return reaction.id

    def get_post_details(self, post_id: int) -> UserPostDto:

        post = Post.objects.select_related('person').get(id=post_id)

        post_reactions = Reaction.objects.filter(post_id=post_id).values_list(
            'react_type', flat=True)

        post_comments = Comment.objects.filter(
            post_id=post_id).select_related('person').prefetch_related(
            Prefetch('comment_set', to_attr='replies'))

        comment_ids_list = []

        for comment in post_comments:
            comment_ids_list.append(comment.id)
            for reply in comment.replies:
                comment_ids_list.append(reply.id)

        comment_reactions = Reaction.objects.filter(
            comment_id__in=comment_ids_list).values('comment_id', 'react_type')

        post_dto = PostDto(post.id, post.person.id, post.post_content,
                           post.posted_at)

        reactions_dto_list = self.create_reactions_dto_list(post_id,
                                                            post_reactions,
                                                            comment_reactions)
        persons_dto_list, comments_dto_list = \
            self.create_persons_dto_list_and_comments_dto_list(
                post.person, post_comments)

        user_post_dto = UserPostDto(post_dto, persons_dto_list,
                                    reactions_dto_list,
                                    comments_dto_list)
        return user_post_dto

    def create_reactions_dto_list(self, post_id, post_reactions,
                                  comment_reactions):

        reactions_dto_list = []

        for reaction in post_reactions:
            reactions_dto_list.append(
                ReactionDto(post_id=post_id, reaction_type=reaction))

        for reaction in comment_reactions:
            reactions_dto_list.append(
                ReactionDto(comment_id=reaction['comment_id'],
                            reaction_type=reaction['react_type']))

        return reactions_dto_list

    def create_persons_dto_list_and_comments_dto_list(self, posted_person,
                                                      comments_for_post):
        persons_dto_list = []
        comments_dto_list = []

        persons_dto_list.append(self.create_person_dto(posted_person))

        for comment in comments_for_post:
            persons_dto_list.append(self.create_person_dto(comment.person))
            comments_dto_list.append(self.create_comment_dto(comment))
            for reply in comment.replies:
                persons_dto_list.append(self.create_person_dto(reply.person))
                comments_dto_list.append(self.create_reply_dto(reply))

        return persons_dto_list, comments_dto_list

    def create_comment_dto(self, comment):

        comment_dto = CommentDto(comment.id, comment.person.id,
                                 comment.comment_at,
                                 comment.comment_content,
                                 post_id=comment.post_id)

        return comment_dto

    def create_reply_dto(self, reply):

        comment_dto = CommentDto(reply.id, reply.person.id, reply.comment_at,
                                 reply.comment_content,
                                 commented_on_id=reply.reply_id)
        return comment_dto

    def create_person_dto(self, person):

        person_dto = PersonDto(person.id, person.username,
                               person.profilePicUrl)
        return person_dto

    def get_user_posts(self, person_id: int, offset: int,
                       limit: int) -> List[UserPostDto]:

        posts_with_user_id = Post.objects.filter(person_id=person_id)[
                             offset:offset + limit].values('id')

        user_posts_list = []

        for post in posts_with_user_id:
            user_posts_list.append(self.get_post_details(post['id']))

        return user_posts_list
