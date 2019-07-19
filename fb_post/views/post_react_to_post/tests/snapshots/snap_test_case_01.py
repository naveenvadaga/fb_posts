# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01PostReactToPostAPITestCase::test_case status'] = 200

snapshots['TestCase01PostReactToPostAPITestCase::test_case body'] = {
    'id': 1
}

snapshots['TestCase01PostReactToPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '8',
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

snapshots['TestCase01PostReactToPostAPITestCase::test_case reaction_type'] = 'haha'

snapshots['TestCase01PostReactToPostAPITestCase::test_case person_username'] = 'username'

snapshots['TestCase01PostReactToPostAPITestCase::test_case count'] = 1
