#sql.py - Create a SQLite3 table and popluate it with data

import sqlite3

#create a new database if the database doesn't already exist

with sqlite3.connect("blog.db")as connection:
    #get a cursor object used to execute sql commands

    c = connection.cursor()

    #create the table
    c.execute("""CREATE TABLE posts
             (title TEXT, post TEXT)
             """)

    #insert dummy data to the table

    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES ("Well", "I\'m well")')
    c.execute('INSERT INTO posts VALUES ("Excellent","I\'m excellent")')
    c.execute('INSERT INTO posts VALUES ("OKAY", "I\'m okay.")')


