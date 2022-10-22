import pytest


class TestCRUD:
    def test_connection(self, db):
        print("using db")
        db.write("Instance 1!\n")

    def test_connection2(self, db):
        print("using db")
        db.write("Instance 2!\n")


class TestCRUD_in_module:
    def test_connection(self, db):
        print("using db")
        db.write("Instance 3!\n")
