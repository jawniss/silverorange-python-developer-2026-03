import json
import sqlite3
from pathlib import Path

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

authorsColumns = [
    "id",
    "full_name",
    "created_at",
    "modified_at"
]

postsColumns = [
    "id",
    "title",
    "body",
    "created_at",
    "modified_at",
    "published_at",
    "author"
]

authorsDataPath = Path("data/authors")
postsDataPath = Path("data/posts")

# Stretch goal: these processes are very similar for the authors and posts, make it a function and pass in args
# Assuming for now these are only run once, otherwise data would repeat
cursor.execute("DELETE FROM authors;")
cursor.execute("DELETE FROM posts;")
for fileName in authorsDataPath.iterdir():
    if fileName.is_file():
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                # Dict class
                fileData = json.load(file)
            # authorsValues = [fileData["id"], fileData["full_name"], fileData["created_at"], fileData["modified_at"]]
            # cursor.execute(f"INSERT INTO authors {authorsColumns} VALUES {authorsValues}")
            # It looks like the timestamps are auto converted from the JSON str to Datetime in the db.sqlite3
            try:
                # Was getting errors with f strings, stretch goal figure that out
                cursor.execute("""
                            INSERT INTO authors (id, full_name, created_at, modified_at) 
                            VALUES (?, ?, ?, ?)
                            """,
                            (fileData["id"], fileData["full_name"], fileData["created_at"], fileData["modified_at"])
                            )
                conn.commit()
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                conn.rollback()
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON from the file. Details: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

for fileName in postsDataPath.iterdir():
    if fileName.is_file():
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                fileData = json.load(file)
            try:
                cursor.execute("""
                            INSERT INTO posts (id, title, body, created_at, modified_at, published_at, author) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """,
                            (fileData["id"], fileData["title"], fileData["body"], fileData["created_at"], fileData["modified_at"], fileData["published_at"], fileData["author"])
                            )
                conn.commit()
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                conn.rollback()
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON from the file. Details: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

conn.close()