from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb.presenters.json_presenter import Presenter
    from fb.storages.storage import StorageClass
    from fb.interactors.react_interactor import ReactionInteractor

    comment_id = kwargs['comment_id']
    user = kwargs['user']
    reaction_type = kwargs['request_data']['reaction_type']

    json_presenter = Presenter()
    storage = StorageClass()

    reaction_interactor = ReactionInteractor(json_presenter, storage)
    response = reaction_interactor.react_to_comment_interactor(user.id, comment_id, reaction_type)
    return response
