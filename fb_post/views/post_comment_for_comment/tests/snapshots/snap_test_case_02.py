# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case status'] = 200

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case body'] = {
    'id': 3
}

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case header_params'] = {
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

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case count'] = 1

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case comment_content'] = 'string1'

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case comment_person'] = 'username'

snapshots['TestCase02PostCommentForCommentAPITestCase::test_case reply_name'] = 1
