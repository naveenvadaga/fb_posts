from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb.presenters.json_presenter import JsonPresenter
    from fb.storages.storage import StorageImplementer
    from fb.interactors.reaction_interactor import ReactionInteractor
    post_id = kwargs['post_id']
    user = kwargs['user']
    reaction_type = kwargs['request_data']['reaction_type']
    json_presenter = JsonPresenter()
    storage = StorageImplementer()
    reaction_interactor = ReactionInteractor(json_presenter, storage)
    response = reaction_interactor.react_to_post(user.id, post_id, reaction_type)
    return response
