import sqlite3
import pandas as pd

def createdb():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        sqlite_create_table_query = '''CREATE TABLE surveyinfo (
                                    name varchar(255),
                                    email varchar(255),
                                    date datetime,
                                    socialmedia varchar(255),
                                    timeperiod varchar(255),
                                    priceing  varchar(255));'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#createdb()

def update(data={'name':'pradeep', 'email':'odelapradeep12@gmail.com','date':'19-07-2022','socialmedia':'instagram','timeperiod':'morethan 1 year','priceing':'reasonable'}):

    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("INSERT INTO surveyinfo VALUES(:name, :email, :date, :socialmedia, :timeperiod, :priceing)", data)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#update(data={'name':'harini', 'email':'odelapradeep12@gmail.com','date':'19-07-2022','socialmedia':'instagram','timeperiod':'morethan 1 year','priceing':'reasonable'})
def getall():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT * FROM surveyinfo")
        data = cursor.fetchall()
        data = pd.DataFrame(data, columns=['name', 'email', 'date', 'socialmedia', 'timeperiod', 'priceing'])
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        return data
print(getall())

