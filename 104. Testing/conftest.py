"""
File with global fixtures
"""
import pytest


@pytest.fixture(scope="function")  # session, module, class, function
def db():
    print("\nOpening DB connection\n")
    connection = open("file.txt", "a")
    connection.write("File opened\n")
    try:
        yield connection
    finally:
        print("\nClosing DB connection\n")
        connection.write("File closed\n")
        connection.close()
