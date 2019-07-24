import pytest
from fb_post.models_utility_functions import *


@pytest.fixture()
def person_fixture():
    person = Person(username="person")
    person.save()
    return person


@pytest.fixture()
def persons_fixture():
    person1 = Person.objects.create(username="person1")
    person2 = Person.objects.create(username="person2")
    person3 = Person.objects.create(username="person3")
    person4 = Person.objects.create(username="person4")
    person5 = Person.objects.create(username="person5")
    return person1, person2, person3, person4, person5


@pytest.fixture()
def comment_fixture(person_fixture, post_fixture):
    comment = Comment.objects.create(post_id=post_fixture.id, person_id=person_fixture.id, comment_content="")
    return comment


@pytest.fixture()
def reply_fixture(comment_fixture, person_fixture):
    reply = Comment.objects.create(reply_id=comment_fixture.id, person_id=person_fixture.id, comment_content="")
    return reply


@pytest.fixture()
def post_fixture(person_fixture):
    post = Post.objects.create(person_id=person_fixture.id, post_content="content")
    return post


@pytest.fixture()
def react_to_comment_fixture(person_fixture, comment_fixture):
    react = React(person=person_fixture, comment_id=comment_fixture.id, react_type="wow")
    react.save()
    return react


@pytest.fixture()
def react_to_post_fixture(person_fixture, post_fixture):
    react = React(person=person_fixture, post_id=post_fixture.id, react_type="haha")
    react.save()
    return react
