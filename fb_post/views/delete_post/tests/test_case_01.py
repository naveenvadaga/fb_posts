"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
RESPONSE_BODY = '{"response": "Invalid post id","http_status_code": 400, "res_status": "INVALID_POST_ID"}'

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },

    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 400
    }
}


class TestCase01DeletePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01DeletePostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                              URL_SUFFIX,
                                                              TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import create_post, react_to_post
        self.foo_user = self._create_user("username", "password")
        self.post = create_post(self.foo_user.id, "content")
        id = self.post.id
        self.post.delete()
        TEST_CASE['request']['path_params']['post_id'] = id
        super(TestCase01DeletePostAPITestCase, self).test_case()
