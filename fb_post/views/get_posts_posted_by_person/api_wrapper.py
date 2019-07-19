from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_id']
    from fb_post.models_utility_functions import get_user_posts

    posts_posted_by_usesr = get_user_posts(user_id)
    print(posts_posted_by_usesr)

    return posts_posted_by_usesr
