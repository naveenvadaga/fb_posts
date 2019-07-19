from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb_post.models_utility_functions import get_total_reaction_count
    total_reactions = {"count": get_total_reaction_count()}

    return total_reactions
