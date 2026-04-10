import sqlite3
import os
class DBConnector:
    """A simple database connector for SQLite."""

    def __init__(self, db_path: str):
        """Initialize the database connection."""
        self.db_path = db_path(need to mention db path in config file)
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found: {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)

    def execute_query(self, query: str, params: tuple = ()):
        """Execute a SQL query and return the results."""
        if self.connection is None:
            raise ConnectionError("Database connection is not established.")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None  

can pas specific sql query using above method and get the result in test case to verify the data in database.   Example usage in test case: