from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    from fb_post.models_utility_functions import get_reaction_metrics
    metrics_dict = get_reaction_metrics(post_id)
    response_object = []
    for key in metrics_dict:
        response_object.append({
            "type": {key},
            "count": metrics_dict[key]
        })
    response={"reactions":response_object}
    print(response_object)
    from django.http.response import HttpResponse

    return response
