from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb.presenters.json_presenter import Presenter
    from fb.storages.storage import StorageClass
    from fb.interactors.post_interactor import PostInteractor
    post_content = kwargs['request_data']['content']
    person = kwargs['user']
    json_presenter = Presenter()
    storage = StorageClass()
    post_interactor = PostInteractor(json_presenter, storage)
    response = post_interactor.create_post_interactor(person.id, post_content)
    return response
