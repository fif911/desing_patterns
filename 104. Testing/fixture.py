import random

import pytest



@pytest.fixture
def rand_obj_gen():
    return random.Random(999)  # lock rand seed


@pytest.fixture
def random_number(rand_obj_gen):
    return rand_obj_gen.random()


def test_random_number(random_number):
    assert random_number


# -------------------
@pytest.fixture
def fixture_dependent_on_rand_num1(random_number):
    return random_number


@pytest.fixture
def fixture_dependent_on_rand_num2(random_number):
    return random_number


def test_two_different_fixtures_dependent_on_random_number_fixture(
        fixture_dependent_on_rand_num1,
        fixture_dependent_on_rand_num2):
    assert fixture_dependent_on_rand_num1 == fixture_dependent_on_rand_num2


# FIXTURES ARE CALCULATED ONCE
# -------------------

# FIXTURE FACTORIES CAN SOLVE THIS PROBLEM

@pytest.fixture
def make_rnd(rand_obj_gen):
    def maker():
        return rand_obj_gen.random()

    return maker  # return callable


@pytest.fixture
def fixture_dependent_on_rand_num1_(make_rnd):
    return make_rnd()  # fixture is callable


@pytest.fixture
def fixture_dependent_on_rand_num2_(make_rnd):
    return make_rnd()  # fixture is callable


def test_two_different_fixtures_dependent_on_factory_fixture(
        fixture_dependent_on_rand_num1_,
        fixture_dependent_on_rand_num2_):
    with pytest.raises(AssertionError):
        assert fixture_dependent_on_rand_num1_ == fixture_dependent_on_rand_num2_

    assert fixture_dependent_on_rand_num1_ != fixture_dependent_on_rand_num2_


# --------------------------------------
# Such structure means we can pass variables in fixture


@pytest.fixture
def make_rnd_with_param(rand_obj_gen):
    def maker(upper_boundary: int):
        return rand_obj_gen.randint(1, upper_boundary)

    return maker  # return callable


@pytest.fixture
def fixture_dependent_on_rand_num1_param(make_rnd_with_param):
    return make_rnd_with_param(10)  # fixture is callable


@pytest.fixture
def fixture_dependent_on_rand_num2_param(make_rnd_with_param):
    return make_rnd_with_param(1000)  # fixture is callable


def test_two_different_fixtures_dependent_on_factory_fixture_param(
        fixture_dependent_on_rand_num1_param,
        fixture_dependent_on_rand_num2_param):
    print(f"{fixture_dependent_on_rand_num1_param} != {fixture_dependent_on_rand_num2_param}")  # 2 != 918
    assert fixture_dependent_on_rand_num1_param != fixture_dependent_on_rand_num2_param
