from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']

    from fb.presenters.json_presenter import JsonPresenter
    from fb.storages.storage import StorageImplementer
    from fb.interactors.post_interactor import PostInteractor
    json_presenter = JsonPresenter()
    storage = StorageImplementer()
    post_interactor = PostInteractor(json_presenter, storage)
    from django_swagger_utils.drf_server.exceptions import BadRequest
    try:
        post_interactor.delete_post(post_id)
        return
    except BadRequest:
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')
