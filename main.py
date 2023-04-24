import sqlite3

#Syed Fasih, Wel Manasseh, Maksym Kalinin, Samuel Afley

# Driver: Wel Manasseh
# Navigator: Samuel Afley
"""

        
        This  function  will create the table

        Args: None

        """


def make_table():

    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor()

    selection.execute("""CREATE TABLE IF NOT EXISTS contacts (first text, last text, number text) """)

    connection.commit()

    connection.close()



# Driver: Maksym Kalinin
# Navigator: Wel Manasseh
"""

        
        This  function  will be used for adding data to the table

        Args:

        first - a string representing contacts first name
        last - a string representing contacts last name
        number - a string representing contacts phone number

        """


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
"""

        
        This  function  will allow the user to see the records

        Args:None

        """


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
"""

        
        This  function  will allow user to delete data

        Args:

        id - represent which row there is data and where user wants to delete data

        """


def delete(id):

    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor() 

    selection.execute(f"DELETE FROM contacts WHERE rowid = {id}")

    connection.commit()

    connection.close()


# Driver: Samuel Afley
# Navigator: Syed Fasih
"""

        
        This  function  will allow user to update or change information for a contact
        Args:

        first - a string representing contacts first name
        last - a string representing contacts last name
        number - a string representing contacts phone number
        id - The row that the contat will be in

        """


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


make_table()