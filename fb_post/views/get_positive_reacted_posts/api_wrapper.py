from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb_post.models_utility_functions import get_posts_with_more_positive_reactions
    positive_posts = get_posts_with_more_positive_reactions()
    positive_posts_array = []
    for post in positive_posts:
        positive_posts_array.append({'id': post})
    from django.http.response import HttpResponse
    return {"posts": positive_posts_array}
