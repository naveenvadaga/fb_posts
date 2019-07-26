from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    from fb.presenters.json_presenter import Presenter
    from fb.storages.storage import StorageClass
    from fb.interactors.post_interactor import PostInteractor
    json_presenter = Presenter()
    storage = StorageClass()
    post_interactor = PostInteractor(json_presenter, storage)
    response = post_interactor.get_post_metrics_interactor(post_id)
    return response