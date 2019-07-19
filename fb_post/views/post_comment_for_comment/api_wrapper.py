from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    comment_id = kwargs['comment_id']
    # print(comment_id)
    user = kwargs['user'].id
    comment_content = kwargs['request_data']['comment_content']
    print(comment_id)
    from fb_post.models_utility_functions import add_comment, reply_to_comment
    comment = reply_to_comment(comment_id, user, comment_content)
    from django.http.response import HttpResponse

    return {"id": comment.id}
