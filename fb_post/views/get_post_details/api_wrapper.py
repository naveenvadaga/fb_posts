from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.models_utility_functions import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # print(kwargs['post_id'])
    print(get_post(kwargs['post_id']))
    return get_post(kwargs['post_id'])
