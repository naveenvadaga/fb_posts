from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    user = kwargs['user']
    react_type = kwargs['request_data']['reaction_type']
    # print("fasf")
    from fb_post.models_utility_functions import react_to_post
    react = react_to_post(user, post_id, react_type)
    if react == None:
        return

    return {"id": react.id}
