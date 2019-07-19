"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string"
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


class TestCase01PostPostContentAPITestCase(CustomAPITestCase):
    test_case_dict = TEST_CASE
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX

    def test_case(self):
        from fb_post.models_utility_functions import Post
        self.count_before_post = Post.objects.all().count()
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01PostPostContentAPITestCase, self)._assert_snapshots(response)
        from fb_post.models_utility_functions import Post
        count_after_post = Post.objects.all().count()

        import json
        response_body = json.loads(response.content)
        post = Post.objects.get(id=response_body['id'])
        self.assert_match_snapshot(count_after_post - self.count_before_post, name='count')
        self.assert_match_snapshot(post.post_content, name='post_content')
        self.assert_match_snapshot(post.person.username, name='post_person')
