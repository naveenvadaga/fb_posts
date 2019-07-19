"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
RESPONSE_BODY = """
[
   
    {
        "username": "username1",
        "id": 2,
        "profile_pic_url": "https://dummy.url.com/pic.png",
        "reaction_type": "haha"
    },
     {
        "username": "username",
        "id": 1,
        "profile_pic_url": "https://dummy.url.com/pic.png",
        "reaction_type": "love"
    }
]
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234"},
        "query_params": {"offset": "0", "limit": '2'},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 200
    }
}


class TestCase01GetReactionsForPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01GetReactionsForPostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                       URL_SUFFIX,
                                                                       TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import create_post, react_to_post
        self.foo_user = self._create_user("username", "password")
        self.foo_user2 = self._create_user("username1", "password")
        self.foo_user3 = self._create_user("username2", "password")
        self.post = create_post(self.foo_user.id, "content")

        self.react1 = react_to_post(self.foo_user2, self.post.id, "haha")
        self.react2 = react_to_post(self.foo_user, self.post.id, "love")
        self.react3 = react_to_post(self.foo_user3, self.post.id, "sad")
        TEST_CASE['request']['query_params']['offset'] = 0
        TEST_CASE['request']['query_params']['limit'] = 2
        TEST_CASE['request']['path_params']['post_id'] = self.post.id
        super(TestCase01GetReactionsForPostAPITestCase, self).test_case()