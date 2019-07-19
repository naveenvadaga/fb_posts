"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string"
}
"""

RESPONSE_BODY = """
{
    "id": 1
     
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 201
    }
}


class TestCase01PostPostContentAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01PostPostContentAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX,
                                                                   TEST_CASE, *args, **kwargs)

    def test_case(self):
        from fb_post.models_utility_functions import Post
        self.count_before_post = Post.objects.all().count()
        super(TestCase01PostPostContentAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        from fb_post.models_utility_functions import Post
        super(TestCase01PostPostContentAPITestCase, self).compareResponse(response, test_case_response_dict)
        count_after_post = Post.objects.all().count()
        import json
        response_body = json.loads(response.content)
        post = Post.objects.get(id=response_body['id'])
        assert self.count_before_post + 1 == count_after_post
        assert post.post_content == 'string'
        assert post.person == self.foo_user
