from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb.presenters.json_presenter import Presenter
    from fb.storages.storage import StorageClass
    from fb.interactors.comment_interactor import CommentInteractor

    comment_id = kwargs['comment_id']
    user = kwargs['user'].id
    comment_content = kwargs['request_data']['comment_content']
    json_presenter = Presenter()
    storage = StorageClass()
    comment_interactor = CommentInteractor(json_presenter, storage)
    response = comment_interactor.add_reply_to_comment_interactor(comment_id, user, comment_content)
    return response
