# -*- coding: utf-8 -*-

from lettuce import step, world, before
from nose.tools import assert_equals
from app.application import app, USERS
import json


@before.all
def before_all():
    world.app = app.test_client()


@step(u'some users are in the system')
def given_some_users_are_in_the_system(step):
    USERS.update({'michael01': {'name': 'Michael Pretus'}})


@step(u'I retrieve the customer \'([^\']*)\'')
def when_i_retrieve_the_customer_username(step, username):
    world.response = world.app.get('/user/{}'.format(username))


@step(u'I should get a \'([^\']*)\' response')
def then_i_should_get_a_expected_status_code_response(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u'the following user details are returned:')
def and_the_following_user_details_are_returned(step):
    assert_equals([json.loads(world.response.data)], step.hashes)
