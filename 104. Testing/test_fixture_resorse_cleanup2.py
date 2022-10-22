class TestCRUD_in_session:
    def test_connection(self, db):
        print("using db")
        db.write("Instance 4!\n")
