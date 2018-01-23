# coding=utf-8

import MySQLdb


def main():
    # Open database connection
    db = MySQLdb.connect("localhost", "test", "test1234", "test")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print "Database version : %s " % data

    cursor.execute("show status like 'Questions'")
    for row in cursor:
        print(row)

    # disconnect from server
    db.close()

if __name__ == "__main__":
    main()
