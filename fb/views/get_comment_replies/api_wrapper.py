from django.core.exceptions import SuspiciousOperation
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from fb.presenters.json_presenter import Presenter
    from fb.storages.storage import StorageClass
    from fb.interactors.comment_interactor import CommentInteractor
    comment_id = kwargs['comment_id']
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']
    json_presenter = Presenter()
    storage = StorageClass()
    comment_interactor = CommentInteractor(json_presenter, storage)
    try:
        response = comment_interactor.get_comment_replies_interactor(comment_id, offset, limit)
        return response
    except SuspiciousOperation:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid comment id', 'INVALID_COMMENT_ID')
