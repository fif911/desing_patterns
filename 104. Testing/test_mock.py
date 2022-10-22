from unittest.mock import patch

import pytest

from resourses_to_mock import ThirdPartyAPI


@pytest.fixture
def global_mock():
    mocked_fetch_api = patch.object(ThirdPartyAPI, "fetch_api",
                                    return_value="JSON fake object")
    mocked_fetch_api.start()
    yield mocked_fetch_api
    mocked_fetch_api.stop()

# @global_mock
class TestIntegration:
    def test_connection_class(self):
        assert ThirdPartyAPI().fetch_api() == "JSON fake object"

    # def test_connection_class(self):
    #     # Object should be imported
    #     mocked_fetch_api = patch.object(ThirdPartyAPI, "fetch_api",
    #                                     return_value="JSON fake object")
    #     mocked_fetch_api.start()
    #     assert ThirdPartyAPI().fetch_api() == "JSON fake object"
    #     mocked_fetch_api.stop()

    # @patch('resourses_to_mock.fetch_api_function', lambda *args, **kwargs: "JSON fake object")
    # def test_connection_function(self):
    #     assert fetch_api_function() == "JSON fake object"

    # @patch('test_mock.fetch_api_function', lambda *args, **kwargs: "JSON fake object")
    # def test_connection_function2(self):
    #     assert fetch_api_function() == "JSON fake object"
