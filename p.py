def get_post_details(self, post_id: int) -> GetPostDto:
    from django.db.models import Prefetch

    post = Post.objects.filter(id=post_id).select_related('person')
    reactions_to_post = React.objects.filter(post_id=post_id).values('react_type')
    comments_for_post = Comment.objects.filter(post_id=post_id).select_related('person').prefetch_related(
        Prefetch('comment_set', to_attr='replies'))
    comment_id = []
    reply_id = []
    # comments_for_post = comments_for_post[0]
    post = post[0]
    for comment in comments_for_post:
        comment_id.append(int(comment.id))
        for reply in comment.replies:
            reply_id.append(int(reply.id))
    comment_reaction = React.objects.filter(comment_id__in=comment_id).values('comment_id', 'react_type')
    reply_reaction = React.objects.filter(comment_id__in=reply_id).values('comment_id', 'react_type')
    comment_reactions = {}
    for reaction in comment_reaction:
        if int(reaction['comment_id']) in comment_reactions:
            comment_reactions[int(reaction['comment_id'])].add(reaction['react_type'])
        else:
            comment_reactions[int(reaction['comment_id'])] = {reaction['react_type']}

    reply_reactions = {}
    for reaction in reply_reaction:
        if reaction['comment_id'] in reply_reactions:
            reply_reactions[int(reaction['comment_id'])].add(reaction['react_type'])
        else:
            reply_reactions[int(reaction['comment_id'])] = {reaction['react_type']}

    person_dto = PersonDto(post.person.id, post.person.username, post.person.profilePicUrl)
    post_dto = PostDto(post.id, person_dto, post.post_content, post.posted_at)
    reactions_to_post_list = []
    for reaction in reactions_to_post:
        reactions_to_post_list.append(reaction['react_type'])
    reactions_to_post_list = list(set(reactions_to_post_list))
    reaction_type_for_post_dto = ReactionType(reactions_to_post_list, len(reactions_to_post_list))
    comments_list = []
    comment_set = []
    comment_count = 0
    for comment in comments_for_post:
        if comment.id in comment_reactions:
            comment_count = len(comment_reactions[int(comment.id)])
            comment_set = list(comment_reactions[comment.id])
        comment_reaction_type_dto = ReactionType(comment_set, comment_count)
        comment_person_dto = PersonDto(comment.person.id, comment.person.username, comment.person.profilePicUrl)
        comment_dto = CommentDto(comment.id, comment_person_dto, comment.comment_at, comment.comment_content,
                                 comment_reaction_type_dto)

        replies_count = len(comment.replies)
        replies_list = []
        for reply in comment.replies:
            reply_reaction_type = {}
            reply_reaction_count = 0
            if reply.id in comment_reactions:
                reply_reaction_count = len(reply_reactions[reply.id])
                reply_reaction_type = list(reply_reactions[reply.id])
            reply_reactions_dto = ReactionType(reply_reaction_type, reply_reaction_count)
            reply_person_dto = PersonDto(reply.person.id, reply.person.username, reply.person.profilePicUrl)
            reply_dto = CommentDto(reply.id, reply_person_dto, reply.comment_at, reply.comment_content,
                                   reply_reactions_dto)
            replies_list.append(reply_dto)
        post_comments_dto = CommentForPostDetailsDto(comment_dto, replies_count, replies_list)
        comments_list.append(post_comments_dto)

    get_post_dto = GetPostDto(post_dto, reaction_type_for_post_dto, comments_list, len(comments_list))
    return get_post_dto


def get_post_details(self, post_id: int) -> GetPostDto:
    from django.db.models import Prefetch

    post = Post.objects.filter(id=post_id).select_related('person')
    reactions_to_post = React.objects.filter(post_id=post_id).values('react_type')
    comments_for_post = Comment.objects.filter(post_id=post_id).select_related('person').prefetch_related(
        Prefetch('comment_set', to_attr='replies'))

    comment_id = []
    reply_id = []
    post = post[0]
    for comment in comments_for_post:
        comment_id.append(int(comment.id))
        for reply in comment.replies:
            reply_id.append(int(reply.id))

    comment_reaction = React.objects.filter(comment_id__in=comment_id).values('comment_id', 'react_type')
    reply_reaction = React.objects.filter(comment_id__in=reply_id).values('comment_id', 'react_type')

    comment_reactions = {}
    for reaction in comment_reaction:
        if int(reaction['comment_id']) in comment_reactions:
            comment_reactions[int(reaction['comment_id'])].add(reaction['react_type'])
        else:
            comment_reactions[int(reaction['comment_id'])] = {reaction['react_type']}

    reply_reactions = {}
    for reaction in reply_reaction:
        if reaction['comment_id'] in reply_reactions:
            reply_reactions[int(reaction['comment_id'])].add(reaction['react_type'])
        else:
            reply_reactions[int(reaction['comment_id'])] = {reaction['react_type']}

    person_dto = PersonDto(post.person.id, post.person.username, post.person.profilePicUrl)
    post_dto = PostDto(post.id, person_dto, post.post_content, post.posted_at)

    reactions_to_post_list = []
    for reaction in reactions_to_post:
        reactions_to_post_list.append(reaction['react_type'])
    reactions_to_post_list = list(set(reactions_to_post_list))

    reaction_type_for_post_dto = ReactionType(reactions_to_post_list, len(reactions_to_post_list))
    comments_list = self.comments_dto_list(comments_for_post, comment_reactions, reply_reactions)

    get_post_dto = GetPostDto(post_dto, reaction_type_for_post_dto, comments_list, len(comments_list))
    return get_post_dto


def comments_dto_list(self, comments_for_post, comment_reactions: dict, reply_reactions: dict) -> List[
    CommentForPostDetailsDto]:
    comments_list = []
    comment_set = []
    comment_count = 0
    for comment in comments_for_post:
        if comment.id in comment_reactions:
            comment_count = len(comment_reactions[int(comment.id)])
            comment_set = list(comment_reactions[comment.id])
        comment_reaction_type_dto = ReactionType(comment_set, comment_count)
        comment_person_dto = PersonDto(comment.person.id, comment.person.username, comment.person.profilePicUrl)
        comment_dto = CommentDto(comment.id, comment_person_dto, comment.comment_at, comment.comment_content,
                                 comment_reaction_type_dto)

        replies_count = len(comment.replies)
        replies_list = self.replies_dto_list(comment.replies, comment_reactions, reply_reactions)
        post_comments_dto = CommentForPostDetailsDto(comment_dto, replies_count, replies_list)
        comments_list.append(post_comments_dto)
    return comments_list


def replies_dto_list(self, replies, comment_reactions, reply_reactions):
    replies_list = []
    for reply in replies:
        reply_reaction_type = {}
        reply_reaction_count = 0
        if reply.id in comment_reactions:
            reply_reaction_count = len(reply_reactions[reply.id])
            reply_reaction_type = list(reply_reactions[reply.id])
        reply_reactions_dto = ReactionType(reply_reaction_type, reply_reaction_count)
        reply_person_dto = PersonDto(reply.person.id, reply.person.username, reply.person.profilePicUrl)
        reply_dto = CommentDto(reply.id, reply_person_dto, reply.comment_at, reply.comment_content,
                               reply_reactions_dto)
        replies_list.append(reply_dto)
    return replies_list
