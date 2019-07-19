


RESPONSE_200_JSON = """
[
    {
        "post_id": 1,
        "posted_by": {
            "username": "string",
            "id": 1,
            "profile_pic_url": "string"
        },
        "posted_at": "2099-12-31 00:00:00",
        "post_content": "string",
        "reactions": {
            "type": [
                "string"
            ],
            "count": 1
        },
        "comments": [
            {
                "comment_id": 1,
                "commenter": {
                    "username": "string",
                    "id": 1,
                    "profile_pic_url": "string"
                },
                "commented_at": "2099-12-31 00:00:00",
                "comment_content": "string",
                "replies_count": 1,
                "reactions": {
                    "type": [
                        "string"
                    ],
                    "count": 1
                },
                "replies": [
                    {
                        "comment_id": 1,
                        "commenter": {
                            "username": "string",
                            "id": 1,
                            "profile_pic_url": "string"
                        },
                        "commented_at": "2099-12-31 00:00:00",
                        "comment_content": "string",
                        "reactions": {
                            "type": [
                                "string"
                            ],
                            "count": 1
                        }
                    }
                ]
            }
        ],
        "comments_count": 1
    }
]
"""

