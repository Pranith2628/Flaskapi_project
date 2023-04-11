import sqlite3

connection = sqlite3.connect("movies.sqlite")

cursor = connection.cursor()
sql_query = """CREATE TABLE movie (
    id integer PRIMARY KEY,
    title text NOT NULL,
    director text NOT NULL,
    language text NOT NULL
)"""

cursor.execute(sql_query)
