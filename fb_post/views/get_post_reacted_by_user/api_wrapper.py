from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_id']
    from fb_post.models_utility_functions import get_posts_reacted_by_user
    post_reacted_by_user = get_posts_reacted_by_user(user_id)
    post_array=[]
    for post in post_reacted_by_user:
        post_array.append({"id":post})

    response_object = {"posts": post_array}
    print(response_object)

    return response_object
