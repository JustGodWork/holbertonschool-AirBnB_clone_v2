import unittest
import MySQLdb
"""This module test the sql"""


class TestDescribeFirstTable(unittest.TestCase):
    """class mysql test"""
    def setUp(self):
        """Connect to the test database"""
        self.db_connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="your_password",
            db="test_database"
        )
        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        """Close cursor and connection after each test"""
        self.cursor.close()
        self.db_connection.close()

    def test_describe_first_table(self):
        """Get the initial number of records in the first_table"""
        initial_count = self.get_num_records()

        # Run the SQL script to describe the first_table
        with open("describe_first_table.sql", "r") as file:
            describe_query = file.read()

        self.cursor.execute(describe_query)

        """Get the number of records in the
        first_table after executing the script"""
        final_count = self.get_num_records()

        # Check if the difference is +1
        difference = final_count - initial_count
        self.assertEqual(difference, 1,
                         "Number of records didn't increase by one.")

    def get_num_records(self):
        """get the number of records"""
        self.cursor.execute("SELECT COUNT(*) FROM first_table")
        return self.cursor.fetchone()[0]


if __name__ == '__main__':
    unittest.main()
