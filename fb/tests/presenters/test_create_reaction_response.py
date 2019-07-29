import unittest
from fb.presenters.json_presenter import *


class TestCreateReaction(unittest.TestCase):

    def test_create_reaction_response(self):
        reaction_id = 1

        json_presenter = JsonPresenter()
        response = json_presenter.create_reaction_response(reaction_id)

        assert response['id'] == reaction_id
