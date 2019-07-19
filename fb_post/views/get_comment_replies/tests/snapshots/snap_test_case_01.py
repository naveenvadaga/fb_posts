# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCommentRepliesAPITestCase::test_case status'] = 200

snapshots['TestCase01GetCommentRepliesAPITestCase::test_case body'] = [
    {
        'comment_content': 'reply1',
        'comment_id': 2,
        'commented_at': '2012-01-14 03:21:34',
        'commenter': {
            'id': 2,
            'profile_pic_url': 'https://dummy.url.com/pic.png',
            'username': 'username1'
        }
    },
    {
        'comment_content': 'reply2',
        'comment_id': 3,
        'commented_at': '2012-01-14 03:21:34',
        'commenter': {
            'id': 3,
            'profile_pic_url': 'https://dummy.url.com/pic.png',
            'username': 'username2'
        }
    }
]

snapshots['TestCase01GetCommentRepliesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '351',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
