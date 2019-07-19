"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "reaction_type": "haha"
}
"""
RESPONSE_BODY = """
{
    "id":1
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

    "response": {
        "header_params": {},
        "body": RESPONSE_BODY,
        "status": 200
    }
}


class TestCase01PostReactToCommentAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def __init__(self, *args, **kwargs):
        super(TestCase01PostReactToCommentAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD,
                                                                      URL_SUFFIX,
                                                                      TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        super(TestCase01PostReactToCommentAPITestCase, self).setupUser(username, password)
        from fb_post.models_utility_functions import create_post, add_comment
        self.post = create_post(self.foo_user.id, "content")
        self.comment = add_comment(self.post.id, self.foo_user.id, "comment")
        TEST_CASE['request']['path_params']['comment_id'] = self.comment.id

    def test_case(self):
        from fb_post.models_utility_functions import React

        self.count_before_reaction = React.objects.all().count()

        super(TestCase01PostReactToCommentAPITestCase, self).test_case()

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
