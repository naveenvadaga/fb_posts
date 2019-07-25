from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "reaction_type": "haha"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01PostReactToPostAPITestCase(CustomAPITestCase):
    test_case_dict = TEST_CASE
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX

    def setupUser(self, username, password):
        pass

    def test_case(self):
        from fb_post.models_utility_functions import Reaction
        self.count_before_reaction = Reaction.objects.all().count()
        super(TestCase01PostReactToPostAPITestCase, self).setupUser('username', 'password')
        from fb_post.models_utility_functions import create_post
        self.post = create_post(self.foo_user.id, "content")
        TEST_CASE['request']['path_params']['post_id'] = self.post.id
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01PostReactToPostAPITestCase, self)._assert_snapshots(response)
        from fb_post.models_utility_functions import Reaction
        count_after_reaction = Reaction.objects.all().count()
        import json
        response_body = json.loads(response.content)
        react = Reaction.objects.get(id=response_body['id'])
        self.assert_match_snapshot(react.react_type, name='reaction_type')
        self.assert_match_snapshot(react.person.username, name='person_username')
        self.assert_match_snapshot(count_after_reaction - self.count_before_reaction, name='count')
