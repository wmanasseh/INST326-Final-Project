import sqlite3
import os


# This method is for creating a table for our contact management system It is not giving us any errors as of now
# It will create the record and establish a connection with the database
def make_table( ):


    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor( )

    selection.execute( """ CREATE TABLE IF NOT EXISTS contacts (first text,last text, number text) """ )




    connection.commit( )

    connection.close( )



#This method will be used for adding data to the table
#It is not pushing any errors yet so we are assuming it has no issues for now
# The three varaibles are first(First name), last(last name), and number(Phone number)
#


def adding_data(last, first , number):


    connection = sqlite3.connect("contactManagement.db")

    selection = connection.cursor( )

    selection.execute(f"SELECT * FROM contacts WHERE first = '{first}' AND last ='{last}' AND number ='{number}'")
     

    outcome = selection.fetchall( )




    if len (outcome) == 0 and first != "" and last != "" and number != "":



        selection.execute( "INSERT INTO contacts VALUES (?, ?, ?)", (first, last, number ) )



    connection.commit( )


    connection.close( )





#This method should be able to show all the records in the database

def showing_records():


    connection = sqlite3.connect("contactManagement.db")


    selection = connection.cursor()    


    selection.execute("SELECT rowid, * FROM contacts")

    result = selection.fetchall()


    connection.commit( )

    connection.close( )


    return result





#This method will be used for deleting data from the table
#We have not yet worked on it but know that it will be needed
def delete(id):
    connection = sqlite3.connect("contactManagement.db")


#this method will be used for updating information for a contact that is already in the system
# It should be able to take the ID number fo the contact and update the changes inputted by the user
# We have not yet figured out on how we will start this function
def update(id, first="", last="", number=""):
    connection = sqlite3.connect("contactManagement.db")






