import sqlite3


class Data:

    def createData(self):

        # create a database
        con = sqlite3.connect("final.db")
        cursor = con.cursor()

        # create a table into the database with all the required table column
        create = """ CREATE TABLE IF NOT EXISTS data (
                    productID INTEGER PRIMARY KEY ,
                    productName TEXT NOT NULL,
                    productPrice INTEGER NOT NULL,
                    productCategory TEXT NOT NULL
                ); """

        cursor.execute(create)

        # insert data into the table and execute all of it at once
        product_data = [(1, 'MacBook Pro', 1400, "Electronics"),
                        (2, 'Final Cut Pro', 299, "Software"),
                        (3, 'Brother MFC-J5855DW printer', 499, "Electronics")]

        cursor.executemany("INSERT INTO data VALUES (?,?,?,?)", product_data)

        show_data = cursor.execute("SELECT productID, productName, productPrice, productCategory FROM data").fetchall()

        # return the data information
        return show_data
