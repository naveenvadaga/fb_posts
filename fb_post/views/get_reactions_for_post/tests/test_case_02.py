"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234"},
        "query_params": {"offset": "0", "limit": '2'},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },

}


class TestCase02GetReactionsForPostAPITestCase(CustomAPITestCase):
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
        self.foo_user3 = self._create_user("username2", "password")
        self.post = create_post(self.foo_user.id, "content")
        self.post2 = create_post(self.foo_user2.id, "comment")

        self.react1 = react_to_post(self.foo_user2, self.post.id, "haha")
        self.react2 = react_to_post(self.foo_user, self.post.id, "love")
        self.react3 = react_to_post(self.foo_user3, self.post.id, "sad")
        self.react4 = react_to_post(self.foo_user2, self.post2.id, "haha")
        TEST_CASE['request']['query_params']['offset'] = 0
        TEST_CASE['request']['query_params']['limit'] = 3
        TEST_CASE['request']['path_params']['post_id'] = self.post.id
        CustomAPITestCase.test_case_dict = TEST_CASE
        self.default_test_case()
