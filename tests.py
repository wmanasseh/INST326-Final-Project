import unittest
import sqlite3
def make_table():

    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor()

    selection.execute("""CREATE TABLE IF NOT EXISTS contacts (first text, last text, number text) """)

    connection.commit()

    connection.close()



# Driver: Maksym Kalinin
# Navigator: Wel Manasseh


def adding_data(first, last , number):

    connection = sqlite3.connect("contactManagement.db")
    selection = connection.cursor()

    selection.execute(f"SELECT * FROM contacts WHERE first = '{first}' AND last='{last}' AND number='{number}'")
    result = selection.fetchall()

    if len(result) == 0 and first != "" and last !="" and number !="":

        selection.execute("INSERT INTO contacts VALUES (?, ?, ?)", (first, last, number))

    connection.commit()
    connection.close()


# Driver: Samuel Afley
# Navigator: Maksym Kalinin


def showing_records():

    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor()    

    selection.execute("SELECT rowid, * FROM contacts")

    result = selection.fetchall()

    connection.commit()

    connection.close()

    return result


# Driver: Syed Fasih
# Navigator: Wel Manasseh


def delete(id):

    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor() 

    selection.execute(f"DELETE FROM contacts WHERE rowid = {id}")

    connection.commit()

    connection.close()


# Driver: Samuel Afley
# Navigator: Syed Fasih



def update(id, first="", last="", number=""):


    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor()     

    if first != "":
        selection.execute(f"UPDATE contacts SET first='{first}' WHERE rowid = {id}")
    
    if last != "":
        selection.execute(f"UPDATE contacts SET last='{last}' WHERE rowid = {id}")
    
    if number != "":
        selection.execute(f"UPDATE contacts SET number='{number}' WHERE rowid = {id}")

    connection.commit()
    
    connection.close()

class TestContactManagement(unittest.TestCase):
    def test_make_table(self):
        # Test that the table is created successfully
        make_table()
        connection = sqlite3.connect("contactManagement.db")
        selection = connection.cursor()
        selection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
        result = selection.fetchone()
        self.assertEqual(result[0], 'contacts')

        # Test that the table has the correct columns
        selection.execute("PRAGMA table_info(contacts)")
        result = selection.fetchall()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], 'first')
        self.assertEqual(result[1][1], 'last')
        self.assertEqual(result[2][1], 'number')

        connection.close()

    

    

    def test_delete(self):
        # Test that a record is deleted from the table
        connection = sqlite3.connect("contactManagement.db")
        selection = connection.cursor()
        selection.execute("INSERT INTO contacts VALUES ('John', 'Doe', '123456')")
        selection.execute("INSERT INTO contacts VALUES ('Jane', 'Doe', '987654')")
        connection.commit()
        delete(1)
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Doe', '987654'))

        # Test that the function does nothing when given an invalid id
        delete(3)
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Doe', '987654'))

        connection.close()

    def test_update(self):
        # Test that a record is updated with a new first name
        connection = sqlite3.connect("contactManagement.db")
        selection = connection.cursor()
        selection.execute("INSERT INTO contacts VALUES ('John', 'Doe', '123456')")
        update(1, first='Jane')
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Doe', '123456'))

        # Test that a record is updated with a new last name
        update(1, last='Smith')
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Smith', '123456'))

        # Test that a record is updated with a new number
        update(1, number='654321')
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Smith', '654321'))

        # Test that the function does nothing when given an invalid id
        update(2, first='John')
        selection.execute("SELECT * FROM contacts")
        result = selection.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Jane', 'Smith', '654321'))

        connection.close()
if __name__ == '__main__':
    unittest.main()