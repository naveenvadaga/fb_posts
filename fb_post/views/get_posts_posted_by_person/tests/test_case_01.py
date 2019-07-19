"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
RESPONSE_BODY = """
[
    {
        "post_id": 1,
        "posted_by": {
            "username": "username",
            "id": 1,
            "profile_pic_url": "https://dummy.url.com/pic.png"
        },
        "posted_at": "2012-01-14 03:21:34",
        "post_content": "post content",
        "reactions": {
            "type": [                
                "haha"
            ],
            "count": 1
        },
        "comments": [
            {
                "comment_id": 1,
                "commenter": {
                    "username": "username1",
                    "id": 2,
                    "profile_pic_url": "https://dummy.url.com/pic.png"
                },
                "commented_at": "2012-01-14 03:21:34",
                "comment_content": "comment 1",
                "replies_count": 1,
                "reactions": {
                    "type": [
                        "haha"
                    ],
                    "count": 1
                },
                "replies": [
                    {
                        "comment_id": 2,
                        "commenter": {
                            "username": "username2",
                            "id": 3,
                            "profile_pic_url": "https://dummy.url.com/pic.png"
                        },
                        "commented_at": "2012-01-14 03:21:34",
                        "comment_content": "reply for comment",
                        "reactions": {
                            "type": [],
                            "count": 0
                        }
                    }
                ]
            }
        ],
        "comments_count": 1
    }
]

"""

TEST_CASE = {
    "request": {
        "path_params": {"user_id": "1234"},
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


class TestCase01GetPostsPostedByPersonAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01GetPostsPostedByPersonAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                          URL_SUFFIX,
                                                                          TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    @freeze_time("2012-01-14 03:21:34")
    def test_case(self):
        from fb_post.models_utility_functions import create_post, react_to_post, add_comment, react_to_comment, \
            reply_to_comment
        self.foo_user = self._create_user("username", "password")
        self.foo_user1 = self._create_user("username1", "password")
        self.foo_user2 = self._create_user("username2", "password")

        self.post = create_post(self.foo_user.id, "post content")

        self.react1 = react_to_post(self.foo_user1, self.post.id, "haha")
        self.react2 = react_to_post(self.foo_user2, self.post.id, "haha")

        self.comment1 = add_comment(self.post.id, self.foo_user1.id, "comment 1")
        self.react_to_comment1 = react_to_comment(self.foo_user, self.comment1.id, "haha")

        self.reply_to_comment1 = reply_to_comment(self.comment1.id, self.foo_user2.id, "reply for comment")
        self.react_to_comment1 = react_to_comment(self.foo_user1, self.reply_to_comment1.id, "haha")

        TEST_CASE['request']['path_params']['user_id'] = self.foo_user.id

        super(TestCase01GetPostsPostedByPersonAPITestCase, self).test_case()

    # def compareResponse(self, response, test_case_response_dict):
    #     import json
    #     response_body = json.loads(response.content)
    #     response_body = response_body[0]
    #     assert response_body['post_id'] == self.post.id
    #     assert response_body['posted_by']["username"] == self.foo_user.username
    #     assert response_body['posted_by']['id'] == self.foo_user.id
    #     assert response_body['posted_by']['profile_pic_url'] == self.foo_user.profilePicUrl
    #     assert response_body['post_content'] == self.post.post_content
    #     assert response_body['posted_at'] == self.post.posted_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert response_body['reactions']['count'] == 2
    #     assert set(response_body['reactions']['type']) == set(['love', 'haha'])
    #     comments = response_body['comments']
    #     assert comments[0]["comment_id"] == self.comment1.id
    #     assert comments[0]["commenter"]["username"] == self.foo_user1.username
    #     assert comments[0]["commenter"]["id"] == self.foo_user1.id
    #     assert comments[0]["commenter"]["profile_pic_url"] == self.foo_user1.profilePicUrl
    #     assert comments[0]["commented_at"] == self.comment1.comment_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert comments[0]["comment_content"] == self.comment1.comment_content
    #     assert comments[0]["replies_count"] == 1
    #     assert comments[0]["reactions"]["type"] == ["haha"]
    #     assert comments[0]["reactions"]["count"] == 1
    #     replies = comments[0]['replies'][0]
    #     assert replies["comment_id"] == self.reply_to_comment1.id
    #     assert replies["commenter"]["username"] == self.foo_user2.username
    #     assert replies["commenter"]["id"] == self.foo_user2.id
    #     assert replies["commenter"]["profile_pic_url"] == self.foo_user2.profilePicUrl
    #     assert replies['commented_at'] == self.reply_to_comment1.comment_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert replies['comment_content'] == self.reply_to_comment1.comment_content
    #     assert replies['reactions']['type'] == []
    #     assert replies['reactions']['count'] == 0
    #     assert response_body['comments_count'] == 1
