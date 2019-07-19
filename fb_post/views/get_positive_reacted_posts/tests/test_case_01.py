"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
RESPONSE_BODY = """
{
    "posts": [
        {
            "id": 1
        }
    ]
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
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


class TestCase01GetPositiveReactedPostsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01GetPositiveReactedPostsAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                           URL_SUFFIX,
                                                                           TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import create_post, react_to_post
        self.foo_user = self._create_user("username", "password")
        self.foo_user2 = self._create_user("username1", "password")
        self.foo_user3 = self._create_user("username2", "password")
        self.foo_user4 = self._create_user("username3", "password")
        self.foo_user5 = self._create_user("username4", "password")
        self.foo_user6 = self._create_user("username5", "password")
        self.post = create_post(self.foo_user.id, "content")
        self.post2 = create_post(self.foo_user2.id, "content")
        self.post3 = create_post(self.foo_user3.id, "content")

        self.react1_for_post = react_to_post(self.foo_user2, self.post.id, "haha")
        self.react2_for_post = react_to_post(self.foo_user, self.post.id, "love")
        self.react3_for_post = react_to_post(self.foo_user3, self.post.id, "haha")
        self.react4_for_post = react_to_post(self.foo_user5, self.post.id, "sad")

        self.react1_for_post2 = react_to_post(self.foo_user2, self.post2.id, "sad")
        self.react2_for_post2 = react_to_post(self.foo_user, self.post2.id, "angry")
        self.react3_for_post2 = react_to_post(self.foo_user3, self.post.id, "haha")
        self.react4_for_post2 = react_to_post(self.foo_user5, self.post.id, "wow")

        self.react1_for_post3 = react_to_post(self.foo_user2, self.post2.id, "haha")
        self.react2_for_post3 = react_to_post(self.foo_user, self.post2.id, "angry")
        self.react3_for_post3 = react_to_post(self.foo_user4, self.post2.id, "angry")
        self.react4_for_post3 = react_to_post(self.foo_user5, self.post2.id, "sad")


        print(self.react1_for_post.id)
        super(TestCase01GetPositiveReactedPostsAPITestCase, self).test_case()
