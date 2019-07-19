from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.models_utility_functions import Post


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_content = kwargs['request_data']['content']
    person = kwargs['user']

    # created_post = create_post(person, comment_content)
    post_created = Post(person=person, post_content=post_content)
    post_created.save()
    from django.http.response import HttpResponse
    import json
    return HttpResponse(json.dumps({'id': post_created.id}),status=201)
