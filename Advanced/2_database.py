#In this tutorial, we will use the sqlite3 module in Python to create a SQLite database, define a table, 
#insert data into the table, and perform a simple query
import sqlite3
# Connect to SQLite database or create if it doesn't exist
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
               first_name TEXT,
               last_name TEXT,
               age INTEGER
)              
 """)

cursor.execute("""
INSERT INTO persons VALUES
               ('Ram','Gupta',45),
               ('Lakshmi','gupta','46'),
               ('rahul','singh',78)
 """)

cursor.execute("""
SELECT first_name FROM persons
WHERE age<50
 """)

rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()