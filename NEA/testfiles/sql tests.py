import sqlite3
try:
    sqliteConnection = sqlite3.connect('test.db')
    cursor = sqliteConnection.cursor()
##        print("Successfully Connected to SQLite")
##        now = datetime.now()
##        joindate = now.strftime("%Y-%m-%d %H:%M:%S")
##        print(joindate)
##        ID = firstname[0:3].title()+ surname[0:3].title()+now.strftime('%d%m%S')
    sqlite_insert_query = """INSERT INTO tests
VALUES
('jim','roberts')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into test table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
