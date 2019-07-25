"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "reaction_type": "haha"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },

}


class TestCase03PostReactToCommentAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def test_case(self):
        super(TestCase03PostReactToCommentAPITestCase, self).setupUser('username', 'password')
        from fb_post.models_utility_functions import create_post, add_comment, react_to_comment
        self.post = create_post(self.foo_user.id, "content")
        self.comment = add_comment(self.post.id, self.foo_user.id, "comment")
        self.react = react_to_comment(self.foo_user, self.comment.id, "love")
        TEST_CASE['request']['path_params']['comment_id'] = self.comment.id

        from fb_post.models_utility_functions import Reaction
        self.count_before_reaction = Reaction.objects.all().count()
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase03PostReactToCommentAPITestCase, self)._assert_snapshots(response)
        from fb_post.models_utility_functions import Reaction
        count_after_reaction = Reaction.objects.all().count()

        self.assert_match_snapshot(count_after_reaction - self.count_before_reaction, name='count')

    '''
    def compareResponse(self, response, test_case_response_dict):
        super(TestCase01PostReactToCommentAPITestCase, self).compareResponse(response, test_case_response_dict)
        from fb_post.models_utility_functions import React
        count_after_reaction = React.objects.all().count()
        import json
        response_body = json.loads(response.content)
        print(json.loads(test_case_response_dict['body'])['id'])
        react = React.objects.get(id=response_body['id'])
        assert react.react_type == "haha"
        assert react.person == self.foo_user
        assert self.count_before_reaction + 1 == count_after_reaction
    '''
