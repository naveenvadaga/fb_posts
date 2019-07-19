from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']
    from fb_post.models_utility_functions import get_reactions_to_post

    reactions_for_post = get_reactions_to_post(post_id, offset, limit)

    return reactions_for_post
