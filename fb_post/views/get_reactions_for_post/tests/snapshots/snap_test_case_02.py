# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetReactionsForPostAPITestCase::test_case status'] = 200

snapshots['TestCase02GetReactionsForPostAPITestCase::test_case body'] = [
    {
        'id': 2,
        'profile_pic_url': 'https://dummy.url.com/pic.png',
        'reaction_type': 'haha',
        'username': 'username1'
    },
    {
        'id': 1,
        'profile_pic_url': 'https://dummy.url.com/pic.png',
        'reaction_type': 'love',
        'username': 'username'
    },
    {
        'id': 3,
        'profile_pic_url': 'https://dummy.url.com/pic.png',
        'reaction_type': 'sad',
        'username': 'username2'
    }
]

snapshots['TestCase02GetReactionsForPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '314',
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
