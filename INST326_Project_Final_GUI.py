import main

from tkinter import ttk

from tkinter import *



display = Tk()

display.geometry("800x700")



frameone = Frame(display)

frameone.place(x = 50, y = 10)

frametwo = Frame(display)

frametwo.place(x = 50, y = 10)



hud = ttk.Treeview ( frameone, height = 30 )

hud.pack()



scrollbar = ttk.Scrollbar(frametwo, orient = "vertical", command = hud.yview)

scrollbar.pack()


# Define number of columns

hud["columns"] = ("1", "2", "3", "4")



# Define headings

hud['show'] = 'headings'



# Assigning the width & anchor to columns

hud.column("1", width = 200, anchor ='c')

hud.column("2", width = 210, anchor ='c')

hud.column("3", width = 210, anchor ='c')

hud.column("4", width = 210, anchor ='c')


# Assigning the heading names columns

hud.heading("1", text = "ROW ID")

hud.heading("2", text = "First Name")

hud.heading("3", text = "Last Name")

hud.heading("4", text = "Phone Number")

# Driver: Wel Manasseh
# Navigator: Maksym Kalinin
"""

        
        These  functions  will be used for the adding_data, update, and delete methods from 
        the main code file

        Args:

        first - a string representing contacts first name
        last - a string representing contacts last name
        number - a string representing contacts phone number
        id - Respresets the row the contact is on

        """

def adding_data(number, last, first):

    main.adding_data(first, last, number)

    show()


def update(id, number, last, first):

    main.update(id, first, last, number)

    show()



def delete(id):

    main.delete(id)

    show()




labelid = Label(display, text = "ROW ID:")

labelid.place(x = 10, y = 580)

idsubmission = Entry(display, width = 10)

idsubmission.place(x = 80, y = 580)





labelone = Label(display, text = "First Name: ")

labelone.place(x = 10,  y = 610)

firstsubmission = Entry(display,)

firstsubmission.place(x = 80, y = 610)




labellast = Label(display, text = "Last Name: ")

labellast.place(x = 10, y = 640)

lastsubmission= Entry(display,)

lastsubmission.place(x = 80, y = 640)







labelnum = Label(display, text = "Phone: ")

labelnum.place(x = 10, y = 670)

numsubmission= Entry(display,)

numsubmission.place(x = 80, y = 670)








buttonCreate = Button(text = "CREATE", bg = "lightgreen", command = lambda:adding_data(firstsubmission.get(), lastsubmission.get(), numsubmission.get()))
buttonCreate.place(x=720, y=580)





buttonUpdate = Button(text = "UPDATE", bg = "#f38630", command = lambda:update(idsubmission.get(), firstsubmission.get(), lastsubmission.get(), numsubmission.get()))
buttonUpdate.place(x=720, y=610)






buttonDelete = Button(text = "DELETE", bg = "#BC544B", command = lambda:delete(idsubmission.get()))

buttonDelete.place(x=720, y=640)





# Driver: Maksym Kalinin
# Navigator: Samuel Afley

def show():

    global hud

    hud.delete(*hud.get_children())

    for i in main.showing_records():

        hud.insert("" , 'end', values = (i[0], i[1], i[2], i[3]))

show()
display.mainloop()