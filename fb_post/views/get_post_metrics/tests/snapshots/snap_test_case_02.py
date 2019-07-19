# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetPostMetricsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetPostMetricsAPITestCase::test_case body'] = {
    'reactions': [
        {
            'count': 2,
            'type': [
                'haha'
            ]
        }
    ]
}

snapshots['TestCase02GetPostMetricsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '43',
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
