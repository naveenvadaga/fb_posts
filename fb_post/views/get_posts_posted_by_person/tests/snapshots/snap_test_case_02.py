# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetPostsPostedByPersonAPITestCase::test_case status'] = 200

snapshots['TestCase02GetPostsPostedByPersonAPITestCase::test_case body'] = [
    {
        'comments': [
            {
                'comment_content': 'comment 1',
                'comment_id': 1,
                'commented_at': '2012-01-14 03:21:34',
                'commenter': {
                    'id': 2,
                    'profile_pic_url': 'https://dummy.url.com/pic.png',
                    'username': 'username1'
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'haha'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'reply for comment',
                        'comment_id': 2,
                        'commented_at': '2012-01-14 03:21:34',
                        'commenter': {
                            'id': 3,
                            'profile_pic_url': 'https://dummy.url.com/pic.png',
                            'username': 'username2'
                        },
                        'reactions': {
                            'count': 0,
                            'type': [
                            ]
                        }
                    }
                ],
                'replies_count': 1
            }
        ],
        'comments_count': 1,
        'post_content': 'post content',
        'post_id': 1,
        'posted_at': '2012-01-14 03:21:34',
        'posted_by': {
            'id': 1,
            'profile_pic_url': 'https://dummy.url.com/pic.png',
            'username': 'username'
        },
        'reactions': {
            'count': 1,
            'type': [
                'haha'
            ]
        }
    }
]

snapshots['TestCase02GetPostsPostedByPersonAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '712',
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
