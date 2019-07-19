from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    comment_id = kwargs['comment_id']
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']
    from fb_post.models_utility_functions import get_replies_for_comment, SuspiciousOperation
    try:
        replies = get_replies_for_comment(comment_id, offset, limit)
        from django.http.response import HttpResponse
        print(replies)
        return replies
    except SuspiciousOperation:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid comment id', 'INVALID_COMMENT_ID')
