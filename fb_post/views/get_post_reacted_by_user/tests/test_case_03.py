"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"user_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },

}


class TestCase03GetPostReactedByUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import create_post, react_to_post
        self.foo_user = self._create_user("username", "password")
        self.foo_user2 = self._create_user("username1", "password")
        self.foo_user3=self._create_user("username2","password")
        self.post = create_post(self.foo_user2.id, "content")
        self.post2 = create_post(self.foo_user.id, "post 2")

        self.react1 = react_to_post(self.foo_user, self.post.id, "haha")
        self.react2 = react_to_post(self.foo_user2, self.post2.id, "love")
        TEST_CASE['request']['path_params']['user_id'] = self.foo_user3.id
        self.default_test_case()
