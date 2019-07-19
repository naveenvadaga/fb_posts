from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.models_utility_functions import delete_post


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    from fb_post.models_utility_functions import Post, ObjectDoesNotExist
    try:
        Post.objects.get(id=post_id).delete()
        return
    except ObjectDoesNotExist:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')
