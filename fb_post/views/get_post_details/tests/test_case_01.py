"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""
TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },

}


class TestCase01GetPostDetailsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

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
        self.post_reactions_types_set = set()
        self.post_reactions_types_set.add(self.react1.react_type)
        self.post_reactions_types_set.add(self.react2.react_type)

        self.comment1 = add_comment(self.post.id, self.foo_user1.id, "comment 1")
        self.react_to_comment1 = react_to_comment(self.foo_user, self.comment1.id, "haha")
        self.comment_reactions_types_set = set()
        self.comment_reactions_types_set.add(self.react_to_comment1.react_type)

        self.reply_to_comment1 = reply_to_comment(self.comment1.id, self.foo_user2.id, "reply for comment")
        self.react_to_comment1 = react_to_comment(self.foo_user1, self.reply_to_comment1.id, "haha")
        self.reply_reactions_types_set = set()
        self.comments_count = 1
        self.reply_count = 1
        TEST_CASE['request']['path_params']['post_id'] = self.post.id

        self.default_test_case()

    # def compareResponse(self, response, test_case_response_dict):
    #     import json
    #     response_body = json.loads(response.content)
    #     comments = response_body['comments']
    #     replies = comments[0]['replies'][0]
    #     # print(response_body)
    #     assert response_body['post_id'] == self.post.id
    #     assert response_body['posted_by']["username"] == self.foo_user.username
    #     assert response_body['posted_by']['id'] == self.foo_user.id
    #     assert response_body['posted_by']['profile_pic_url'] == self.foo_user.profilePicUrl
    #     assert response_body['post_content'] == self.post.post_content
    #     assert response_body['posted_at'] == self.post.posted_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert response_body['reactions']['count'] == len(self.post_reactions_types_set)
    #     assert set(response_body['reactions']['type']) == self.post_reactions_types_set
    #     comment_ids = [comment['comment_id'] for comment in comments]
    #     replies_ids = []
    #     assert self.comment1.id in comment_ids
    #     comment_data = {}
    #     for comment in comments:
    #         if comment['comment_id'] == self.comment1.id:
    #             comment_data = comment
    #             replies_ids = [reply["comment_id"] for reply in comment['replies']]
    #     assert comment_data["comment_id"] == self.comment1.id
    #     assert comment_data["commenter"]["username"] == self.foo_user1.username
    #     assert comment_data["commenter"]["id"] == self.foo_user1.id
    #     assert comment_data["commenter"]["profile_pic_url"] == self.foo_user1.profilePicUrl
    #     assert comment_data["commented_at"] == self.comment1.comment_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert comment_data["comment_content"] == self.comment1.comment_content
    #     assert comment_data["replies_count"] == self.reply_count
    #     assert comment_data["reactions"]["type"] == list(self.comment_reactions_types_set)
    #     assert comment_data["reactions"]["count"] == len(self.comment_reactions_types_set)
    #     assert self.reply_to_comment1.id in replies_ids
    #     for reply in comment['replies']:
    #         if reply["comment_id"] == self.reply_to_comment1.id:
    #             replies = reply
    #     assert replies["comment_id"] == self.reply_to_comment1.id
    #     assert replies["commenter"]["username"] == self.foo_user2.username
    #     assert replies["commenter"]["id"] == self.foo_user2.id
    #     assert replies["commenter"]["profile_pic_url"] == self.foo_user2.profilePicUrl
    #     assert replies['commented_at'] == self.reply_to_comment1.comment_at.strftime("%Y-%m-%d %H:%M:%S")
    #     assert replies['comment_content'] == self.reply_to_comment1.comment_content
    #     assert replies['reactions']["type"] == list(self.reply_reactions_types_set)
    #     assert replies['reactions']['count'] == len(self.reply_reactions_types_set)
    #     assert response_body['comments_count'] == self.comments_count
