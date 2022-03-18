# [HOME](README.md#testing) Testing

# Testing Types

## Black Box Testing

Testing without knowledge of the internal workings of the item being tested.
Tests are usually functional.

## White Box Testing

Testing based on an analysis of internal workings and structure of a piece of
software. Includes techniques such as Branch Testing and Path Testing. Also
known as Structural Testing and Glass Box Testing.

## Functional Testing

Validating an application or Web site conforms to its specifications and 
correctly performs all its required functions. This entails a series of tests
which perform a feature by feature validation of behavior, using a wide range
of normal and erroneous input data. This can involve testing of the product's
user interface, APIs, database management, security, installation, networking,
etc. Functional testing can be performed on an automated or manual basis using
black box or white box methodologies.

## Acceptance Testing

Testing to verify a product meets customer's specified requirements.
A customer usually does this type of testing on a product that is developed
externally.

## Compatibility Testing

Testing to ensure compatibility of an application or Web site with different
browsers, OSs, and hardware platforms. Compatibility testing can be performed
manually or can be driven by an automated functional or regression test suite.

## Conformance Testing

Verifying implementation conformance to industry standards. Producing tests
for the behavior of an implementation to be sure it provides the portability,
interoperability, and/or compatibility a standard defines.

## Integration Testing

Testing in which modules are combined and tested as a group. Modules are
typically code modules, individual applications, client and server
applications on a network, etc. Integration Testing follows unit testing and 
precedes system testing.

Integration testing tests a class while it is integrated with other classes.
For example, assume you are testing CustomerData, which depends on Linq to SQL
and a database connection. In integration testing, you test CustomerData's
methods by calling them and ensuring it does its job properly engaging all the
related classes. Integration test is more popular among developers because it
is really testing the system as it should be. 

Integration testing means you are going to test some class while it is
integrated with other classes and with infrastructure, like the database, file
system, mail server, etc. Whenever you write an integration test, you test a
component's behavior as it should be, without any mock up.
Integration tests are easier to write since there is no mock up. Moreover,
they give additional confidence that the code works as it should, since all
the necessary components and dependencies are in place and are also being
tested.

## Load Testing

Load testing is a generic term covering **Performance Testing** and
**Stress Testing**.

## Performance Testing

Performance testing can be applied to understand your application or web
site's scalability, or to benchmark the performance in an environment of
third party products such as servers and middle-ware for potential purchase.
This sort of testing is particularly useful to identify performance
bottlenecks in high use applications. Performance testing generally
involves an automated test suite as this allows easy simulation of a variety
of normal, peak, and exceptional load conditions. 

## Regression Testing

Similar in scope to a functional test, a regression test allows a consistent,
repeatable validation of each new release of a product or Web site. Such
testing ensures reported product defects have been corrected for each new
release and that no new quality problems were introduced in the maintenance
process. Though regression testing can be performed manually an automated test
suite is often used to reduce the time and resources needed to perform
the required testing.

## Smoke Testing

A quick-and-dirty test that the major functions of a piece of software work
without bothering with finer details. Originated in the hardware testing
practice of turning on a new piece of hardware for the first time and
considering it a success if it does not catch on fire.

## Stress Testing

Testing conducted to evaluate a system or component at or beyond the limits of
its specified requirements to determine the load under which it fails and how.
A graceful degradation under load leading to non-catastrophic failure is the
desired result. Often Stress Testing is performed using the same process as
Performance Testing but employing a very high level of simulated load.

## System Testing

Testing conducted on a complete, integrated system to evaluate the system's
compliance with its specified requirements. System testing falls within
the scope of black box testing, and as such, should require no knowledge of
the inner design of the code or logic.

## Unit Testing

Functional and reliability testing in an Engineering environment. Producing
tests for the behavior of components of a product to ensure their correct
behavior prior to system integration.

One principle to remember during unit testing is: when you are unit testing
a class, you should have no dependency on database, file, registry, web
services, etc. You should be able to test any class in complete "isolation"
and your classes should be designed to support complete "isolation". 

# Test-Driven Development

Also called **TDD**

Test Driven Development (TDD) is an extreme form of unit testing. The general
principle is to first write the unit tests, then write the actual code.

The repetition of a very short development cycle: 
Requirements are turned into very specific test cases, then the software is improved to pass the new tests, only. 
This is opposed to software development that allows software to be added that is not proven to meet requirements.

* Add a test
* Run all tests and see if the new test fails. The new test should fail for the expected reason.
* Write the code that causes the test to pass
* Run tests. If all test cases now pass, the programmer can be confident that the new code 
  meets the test requirements, and does not break or degrade any existing features.
* Refactor code. The growing code base must be cleaned up regularly during test-driven development.
* Repeat

## Frameworks

* Python's builtin [unittest](https://docs.python.org/3/library/unittest.html)
* [nosetests](https://nose.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/latest/) See below

# Behavior-Driven Development

Also called **BDD**

Is an extension of test-driven development development that makes use of a simple, **domain-specific scripting 
language**. These DSLs convert structured natural language statements into executable tests. The result is
a closer relationship to acceptance criteria for a given function and the tests used to validate that functionality.

**BDD** focuses on:
* Where to start in the process
* What to test and what not to test
* How much to test in one go
* What to call the tests
* How to understand why a test fails

For each unit of software, a software developer must:
* Define a test set for the unit first
* Make the tests fail
* Then implement the unit
* Finally verify that the implementation of the unit makes the tests succeed

## Frameworks

* [behave](http://pythonhosted.org/behave/)

# Isolation Frameworks

* [Python Mock](https://docs.python.org/3/library/unittest.mock.html)

# What's the difference between a mock & stub?

**Dummy objects** are passed around but never actually used. Usually they are just used to fill parameter lists.

**Fake objects** actually have working implementations, but usually take some shortcut which makes them
not suitable for production (an in memory database is a good example).

**Stubs** provide canned answers to calls made during the test, usually not responding at all to anything
outside what's programmed in for the test. **Stubs** may also record information about calls, such as
an email gateway stub that remembers the messages it 'sent', or maybe only how many messages it 'sent'.
The pre-written **stub** would follow an **initialize -> exercise -> verify**

**Mocks** are pre-programmed objects with expectations which form a specification of the calls they are
expected to receive. Tests written with mocks usually follow an 
**initialize -> set expectations -> exercise -> verify pattern to testing**.

# [pytest](https://docs.pytest.org/en/latest/)

Training [Python Testing 101 with pytest](https://www.youtube.com/watch?v=etosV2IWBF0)

Tutorial folder: `tutorials/pytest`

## Virtual Environment

Install under Ubuntu:
```bash
sudo apt install python3-venv
```

Create (the `myvenv`-folder will be created):
```bash
python3 -m venv myvenv
```

Activate `myvenv`:
```bash
. myvenv/bin/activate
source myvenv/bin/activate
```

Install `pytest`:
```bash
pip install pytest
```

Run `pytest`
```bash
pytest
```

## [test_example_01](tutorials/pytest/test_example_01.py)

Simple test here

## [test_example_02](tutorials/pytest/test_example_02.py)

Execute test without `Calculator`-class
```
================================================================= test session starts =================================================================
platform linux -- Python 3.8.2, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /home/vantonevych/personal/python/tutorials/pytest
collected 2 items                                                                                                                                     

test_example_01.py .                                                                                                                            [ 50%]
test_example_02.py F                                                                                                                            [100%]

====================================================================== FAILURES =======================================================================
______________________________________________________________________ test_add _______________________________________________________________________

    def test_add():
        # 1. Arrange (setup)
>       calculator = Calculator()
E       NameError: name 'Calculator' is not defined
```

## [test_example_03](tutorials/pytest/test_example_03.py)

One test which passes successfully:

```
...
collected 3 items                                                                                                                                     

test_example_01.py .                                                                                                                            [ 33%]
test_example_02.py F                                                                                                                            [ 66%]
test_example_03.py .                                                                                                                            [100%]
```

## [test_example_04](tutorials/pytest/test_example_04.py)

Contains failing test

```
test_example_04.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <test_example_04.Calculator object at 0x7fa96c1088b0>, x = 2, y = '3'

    def add(self, x, y):
>       return x + y
E       TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## [test_example_05](tutorials/pytest/test_example_05.py)

Use `with pytest.raises(CalculatorException):` for expected exception

Check exception message `with pytest.raises(CalculatorException) as e:`
and `assert str(e.value) == 'can only concatenate str (not "int") to str'`

```
test_example_05.py ..
```

## [test_example_06](tutorials/pytest/test_example_06.py)

Starting from here and below the examples are from this video:
[Продвинутое использование py test, Андрей Светлов, Python Core Developer](https://www.youtube.com/watch?v=7KgihdKTWY4)
[Slides](http://asvetlov.github.io/pytest-slides/#/)

Using `pytest.fixture`

`rnd` is a fixture

## [test_example_07](tutorials/pytest/test_example_07.py)

Using one `pytest.fixture` dependent from other (`rnd` dependent from `rnd_tuple`)

## [test_example_08](tutorials/pytest/test_example_08.py)

A `pytest.fixture` value is **pre-calculated once**, so all test-functions are using the same fixture-value

## [test_example_09](tutorials/pytest/test_example_09.py)

Use **fixture-factory** to return different values (return **decorator-function** `maker()` instead of value)

## [test_example_10](tutorials/pytest/test_example_10.py)

Use `pytest.yield_fixture` for cleanup used resources (like a file)

## [test_example_11](tutorials/pytest/test_example_11.py)

Use **fixtures factory** for cleanup

## [test_example_12](tutorials/pytest/test_example_12.py)

Use in-memory resource fixtures for tests like `sqlite3` and `redis`


TODO:
https://habr.com/ru/post/269759/
http://devork.be/talks/advanced-fixtures/advfix.html
https://levelup.gitconnected.com/advanced-pytest-techniques-i-learned-while-contributing-to-pandas-7ba1465b65eb

## Test Allowed HTTP Methods

```python
from functools import partial
from http import HTTPStatus

import flask
import pytest


@pytest.fixture(scope="session")
def url():
    return partial(flask.url_for, "api.some_namespace_some_resource")


class TestSuite:
    """ Test suite for ... endpoint """

    @pytest.mark.parametrize("method", ("POST", "DELETE", "PATCH", "PUT",))
    def test_check_if_endpoint_exists_required_only_get(self, client, url, method):
        """ Must return METHOD_NOT_ALLOWED to all methods except GET """
        response = getattr(client, method.lower())(url())

        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
```

## Apply Fixture by Name (example for `flask`)

```python
from http import HTTPStatus

import pytest
from pytest import fixture
from requests import Response
from requests.exceptions import RequestException
from werkzeug.exceptions import FailedDependency


ERROR_KEYS = ("code", "message", "details")


@fixture
def mocked_introspection_failed_json_response(mocker):
    """ Patch introspection response """
    result = mocker.patch('my_library.requests.post')
    resp = Response()
    resp.status_code = HTTPStatus.METHOD_NOT_ALLOWED
    resp.json = lambda: {'something': 'happens'}
    result.return_value = resp

    return result


@fixture
def mocked_introspection_failed_text_response(mocker):
    """ Patch introspection response """
    result = mocker.patch('my_library.requests.post')
    resp = Response()
    resp.status_code = HTTPStatus.METHOD_NOT_ALLOWED
    resp._content = b"Something went wrong"
    result.return_value = resp

    return result


@fixture
def mocked_introspection_insufficient_scope_response(mocker):
    """ Patch introspection response """
    result = mocker.patch('my_library.requests.post')
    resp = Response()
    resp.status_code = HTTPStatus.FORBIDDEN
    resp.json = lambda: {"code": HTTPStatus.FORBIDDEN, "message": "FORBIDDEN", "details": None}
    result.return_value = resp

    return result


@fixture
def mocked_introspection_request_exception(mocker):
    """ Patch introspection response with exception """
    result = mocker.patch('my_library.requests.post')
    result.side_effect = RequestException('Mocked exception')

    return result


@pytest.mark.parametrize(
    "mocked_introspection_response,error_status,error_message_partial",
    (
        (
            'mocked_introspection_request_exception',
            HTTPStatus.FAILED_DEPENDENCY,
            'Token introspection failed',
        ),
        (
            'mocked_introspection_insufficient_scope_response',
            HTTPStatus.FORBIDDEN,
            'scope',
        ),
        (
            'mocked_introspection_failed_json_response',
            HTTPStatus.METHOD_NOT_ALLOWED,
            'Token introspection failed',
        ),
        (
            'mocked_introspection_failed_text_response',
            HTTPStatus.METHOD_NOT_ALLOWED,
            'Token introspection failed',
        ),
    ),
)
def test_introspect_error_response(
    identity, valid_token, request, mocked_introspection_response, error_status, error_message_partial
):
    request.getfixturevalue(mocked_introspection_response)

    with pytest.raises(FailedDependency) as e:
        identity.introspect(valid_token)

    response = e.value
    assert response.code == HTTPStatus.FAILED_DEPENDENCY

    data = response.data
    errors = data.get('errors', [])
    assert len(errors) == 1

    error = errors[0]
    assert all(key in error for key in ERROR_KEYS)
    assert error['code'] == error_status
    assert error_message_partial in error['message']
```

## Factory and Sub-Factory

```python
from factory import Sequence, SubFactory, RelatedFactory
from factory.django import DjangoModelFactory, mute_signals


@mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Sequence(lambda n: "user_%d@test.com" % n)
    password = "password"
    profile = RelatedFactory(ProfileFactory, "user")

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)


class DependencyFactory(DjangoModelFactory):
    class Meta:
        model = Dependency

    user = SubFactory("tests.factories.UserFactory")
    parent = SubFactory("tests.factories.UserFactory")
    dependency_relation = Relations.SON_RELATION
    national_id = FuzzyInteger(1000000000, 1999999999)
```

## Fixture with Parameter

```python
@pytest.fixture
def create_dependent(user_factory, parent, dependency_factory):
    def _create_user(dependent_nid):
        return dependency_factory(parent=parent, user=user_factory(), national_id=dependent_nid).user

    return _create_user


@pytest.fixture
def dependent1(create_dependent, dependent1_nid):
    return create_dependent(dependent1_nid)
```

One more:

```python
@pytest.fixture
def assets_folder(root_dir):
    return os.path.join(root_dir, "tests", "assets")


def load_assets_json(assets, filename):
    with open(os.path.join(assets, f"{filename}.json")) as stream:
        return json.load(stream)


@pytest.fixture
def get_assets_json(assets_folder):
    return partial(load_assets_json, assets_folder)


def get_person_info_asset(dependent_nid):
    return f"person_info_{dependent_nid}"


@pytest.fixture
def mock_person_info_dependent_response(
    requests_mock, parent_nid, get_assets_json
):
    def _mock_request(dependent_nid):
        requests_mock.get(
            f"{some_client.get_person_info_url}?ID={dependent_nid}&CallerID={parent_nid}",
            json=get_assets_json(get_person_info_asset(dependent_nid)),
        )

    return _mock_request


@pytest.fixture
def mock_person_info_dependent1_response(
    mock_person_info_dependent_response, dependent1_nid
):
    mock_person_info_dependent_response(dependent1_nid)
```

## Tests with DB

Requirements:

```
pytest==5.4.2
pytest-cov==2.9.0
pytest-env==0.6.2
pytest-spec==2.0.0
pytest-mock==3.1.0
pytest-flask==1.0.0
pytest-factoryboy==2.0.3
pytest-runner==4.2
freezegun==0.3.15
requests-mock==1.8.0
```

```python
import inspect

import factory
import pytest
from pytest_factoryboy import register
from flask_sqlalchemy import SQLAlchemy
from my_app import create_app


# External file
db = SQLAlchemy()


# External file 
class Profile(db.Model):
    """ User's Profile """

    __tablename__ = "profile"

    MALE = "M"
    FEMALE = "F"

    id = db.Column(db.Integer, primary_key=True)
    national_id = db.Column(db.BigInteger, unique=True)
    gender = db.Column(db.String)
    has_hypertension = db.Column(db.Boolean, nullable=True)
    has_diabetes = db.Column(db.Boolean, nullable=True)


class ProfileFactory(factory.alchemy.SQLAlchemyModelFactory):
    national_id = factory.Sequence(lambda n: f'00000{n}')
    gender = "M"

    class Meta:
        model = Profile
        sqlalchemy_session = db.session


register(ProfileFactory)


@pytest.fixture(scope="session")
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture(scope="session")
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture(autouse=True)
def sample_profile(db):
    profile = ProfileFactory(
        national_id="1112223334",
        gender="M",
        has_hypertension=True,
        has_diabetes=True,
    )
    db.session.add(profile)
    db.session.commit()
    return profile


@pytest.fixture(autouse=True)
def cleanup(db):
    """ A little hack that cleans all produced db records after each test function execution """
    yield
    for _, model in inspect.getmembers(my_app.models, inspect.isclass):
        db.session.query(model).delete()

    db.session.commit()
```

## Disable an `autouse=True` fixture for Specific Test Case

```python
@pytest.fixture(autouse=True)
def sample_profile(request, db):
    if 'disable_sample_profile' in request.keywords:
        return

    profile = ProfileFactory(...)
    db.session.add(profile)
    db.session.commit()
    return profile


class TestSuite:
    @pytest.mark.disable_sample_profile
    @pytest.mark.parametrize(
        ("params", "result1", "result2"),
        (
            # Total count
            ({}, 5, 3),

            # Filter by `until`-date
            ({"until": "2020-07-15"}, 0, 0),

            # Filter by `since`-date
            ({"since": "2020-01-01"}, 5, 3),

            # Filter by 'since' and 'until' dates
            ({"since": "2020-01-01", "until": "2020-07-15"}, 0, 0),
        )
    )
    def test_endpoint_return_response_in_correct_format(
        self, client, url, params, result1, result2,
    ):
        pass
```

## Mock Request with JSON Data

```python
import json
import os

import pytest
import urllib
from django.urls import reverse, resolve


@pytest.fixture(scope="session")
def root():
    """ Fixture should return root path for test's assets """
    return os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def get_some_json_response(root):
    filename = os.path.join(
        root, "tests", "assets", "some_response.json"
    )
    with open(filename) as stream:
        return json.load(stream)


# For Django
def get_view_by_reverse(view_id, *args, **kwargs):
    """
        Returns url and view by `view_id`
        :kwargs - dict with url query params
    """
    url = reverse(view_id, args=args)
    view = resolve(url).func
    if kwargs:
        url += f"?{urllib.parse.urlencode(kwargs)}"
    return view, url


# For Django
@pytest.fixture(scope="session")
def view_by_reverse():
    return partial(get_view_by_reverse)


@pytest.fixture
def some_url():
    return view_by_reverse("api:some-action")


@pytest.fixture
def mock_get_some_json_response(requests_mock, some_url, get_some_json_response):
    requests_mock.get(
        some_url,
        json=get_some_json_response,
    )
```

## Simple Patch

```python
import pytest
from external.api import external_api_client


@pytest.fixture
def mock_yakeen_client_retrieve_access_token(mocker):
    return mocker.patch.object(external_api_client, "retrieve_access_token")
```

## Use One or More Fixtures

```python
@pytest.mark.usefixtures("some_fixture")
def test_something():
    pass
```

# Links

* [Python Testing Tools/Frameworks](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)

* [The Little Mocker: a conversation around mocking](https://8thlight.com/blog/uncle-bob/2014/05/14/TheLittleMocker.html)

* [What's the difference between a mock & stub?](https://stackoverflow.com/questions/3459287/whats-the-difference-between-a-mock-stub)

* [Mocks Aren't Stubs, Martin Fowler](https://martinfowler.com/articles/mocksArentStubs.html)

* [Python Testing 101 with pytest](https://www.youtube.com/watch?v=etosV2IWBF0)

* [TODO Lisa Roach - Demystifying the Patch Function](https://youtu.be/ww1UsGZV8fQ)
