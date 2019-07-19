from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print("sdfsa")
    post_id = kwargs['post_id']
    user = kwargs['user'].id
    comment_content = kwargs['request_data']['comment_content']

    from fb_post.models_utility_functions import add_comment
    comment = add_comment(post_id, user, comment_content)

    return {"id": comment.id}
