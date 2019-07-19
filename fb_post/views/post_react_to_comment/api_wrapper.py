from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    comment_id = kwargs['comment_id']
    user = kwargs['user']
    react_type = kwargs['request_data']['reaction_type']
    # print(comment_id)
    from fb_post.models_utility_functions import react_to_comment
    react = react_to_comment(user, comment_id, react_type)
    return {"id": react.id}
