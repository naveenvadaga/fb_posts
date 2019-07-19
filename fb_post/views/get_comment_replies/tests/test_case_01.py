"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from freezegun import freeze_time

REQUEST_BODY = """

"""
RESPONSE_BODY = """
[
    {
        "comment_id": 2,
        "commenter": {
            "username": "username1",
            "id": 2,
            "profile_pic_url": "https://dummy.url.com/pic.png"
        },
        "commented_at": "2012-01-14 03:21:34",
        "comment_content": "reply1"
    },
    {
        "comment_id": 3,
        "commenter": {
            "username": "username2",
            "id": 3,
            "profile_pic_url": "https://dummy.url.com/pic.png"
        },
        "commented_at": "2012-01-14 03:21:34",
        "comment_content": "reply2"
    }
]
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1234"},
        "query_params": {"offset": "0", "limit": '2'},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },

}


class TestCase01GetCommentRepliesAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    @freeze_time("2012-01-14 03:21:34")
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
        TEST_CASE['request']['path_params']['comment_id'] = self.comment.id
        self.default_test_case()

    '''def compareResponse(self, response, test_case_response_dict):
        import json
        response_body = json.loads(response.content)
        print(response_body)
        reply1 = response_body[0]
        reply2 = response_body[1]
        assert reply1['comment_id'] == self.reply1.id
        assert reply1["commenter"]["username"] == self.foo_user1.username
        assert reply1["commenter"]["id"] == self.foo_user1.id
        assert reply1["commenter"]["profile_pic_url"] == self.foo_user1.profilePicUrl
        assert reply1["commented_at"] == self.reply1.comment_at.strftime("%Y-%m-%d %H:%M:%S")
        assert reply1["comment_content"] == self.reply1.comment_content
        assert reply2['comment_id'] == self.reply2.id
        assert reply2['commenter']["username"] == self.foo_user2.username
        assert reply2['commenter']['id'] == self.foo_user2.id
        assert reply2['commenter']['profile_pic_url'] == self.foo_user2.profilePicUrl
        assert reply2['commented_at'] == self.reply2.comment_at.strftime("%Y-%m-%d %H:%M:%S")
        assert reply2['comment_content'] == self.reply2.comment_content '''
