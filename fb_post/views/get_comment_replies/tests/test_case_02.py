"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
RESPONSE_BODY = """{"response": "Invalid post id", "http_status_code": 400, "res_status": "INVALID_POST_ID"}"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1234"},
        "query_params": {"offset": "0", "limit": '2'},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 400
    }
}


class TestCase02GetCommentRepliesAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase02GetCommentRepliesAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                     URL_SUFFIX,
                                                                     TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import create_post, add_comment, reply_to_comment
        self.foo_user = self._create_user("username", "password")
        self.foo_user1 = self._create_user("username1", "password")
        self.foo_user2 = self._create_user("username2", "password")
        self.foo_user3 = self._create_user("username3", "password")
        self.post = create_post(self.foo_user.id, "post content")
        self.comment = add_comment(self.post.id, self.foo_user1.id, "comment 1")
        self.reply1 = reply_to_comment(self.comment.id, self.foo_user1.id, "reply1")
        self.reply2 = reply_to_comment(self.comment.id, self.foo_user2.id, "reply2")
        self.reply3 = reply_to_comment(self.comment.id, self.foo_user3.id, "reply3")
        TEST_CASE['request']['query_params']['offset'] = 0
        TEST_CASE['request']['query_params']['limit'] = 2
        TEST_CASE['request']['path_params']['comment_id'] = self.reply1.id
        super(TestCase02GetCommentRepliesAPITestCase, self).test_case()
