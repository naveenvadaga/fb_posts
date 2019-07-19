"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "comment_content": "string1"
}
"""

RESPONSE_BODY = """
{
    "id": 2
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234", "comment_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 200
    }
}


class TestCase01PostCommentForCommentAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01PostCommentForCommentAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                         URL_SUFFIX,
                                                                         TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import Comment, create_post, add_comment
        self.foo_user = self._create_user("username", "password")
        self.post = create_post(self.foo_user.id, "content")
        self.comment = add_comment(self.post.id, self.foo_user.id, "comment")
        print(self.comment.id)
        print("s")
        TEST_CASE['request']['path_params']['comment_id'] = self.comment.id

        self.count_before_comment = Comment.objects.all().count()
        super(TestCase01PostCommentForCommentAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        super(TestCase01PostCommentForCommentAPITestCase, self).compareResponse(response, test_case_response_dict)
        from fb_post.models_utility_functions import Comment
        count_after_comment = Comment.objects.all().count()
        import json
        print(type(response.content))
        response_body = json.loads(response.content)
        print(type(response_body['id']))
        assert self.count_before_comment + 1 == count_after_comment
        # comment = Comment.objects.get(comment_content='string1')
        # assert comment.comment_content == "string"
        # assert comment.person == self.foo_user
