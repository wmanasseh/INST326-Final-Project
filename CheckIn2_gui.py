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

labelid.place(x = 10, y = 550)

idsubmission = Entry(display, width = 10)

idsubmission.place(x = 80, y = 550)






labelone = Label(display, text = "First Name: ")

labelone.place(x = 140,  y = 550)

firstsubmission = Entry(display,)

firstsubmission.place(x = 218, y = 550)






labellast = Label(display, text = "Last Name: ")

labellast.place(x = 340, y = 550)

lastsubmission= Entry(display,)

lastsubmission.place(x = 410, y = 550)







labelnum = Label(display, text = "Phone: ")

labelnum.place(x = 540, y = 550)

numsubmission= Entry(display,)

numsubmission.place(x = 580, y = 550)








buttonCreate = Button(text = "CREATE", bg = "lightgreen", command = lambda:adding_data(firstsubmission.get(), lastsubmission.get(), numsubmission.get()))
buttonCreate.place(x=720, y=550)





buttonUpdate = Button(text = "UPDATE", bg = "#f38630", command = lambda:update(idsubmission.get(), firstsubmission.get(), lastsubmission.get(), numsubmission.get()))
buttonUpdate.place(x=720, y=585)






buttonDelete = Button(text = "DELETE", bg = "#BC544B", command = lambda:delete(idsubmission.get()))

buttonDelete.place(x=720, y=625)





# Driver: Maksym Kalinin
# Navigator: Samuel Afley

def show():

    global hud

    hud.delete(*hud.get_children())

    for i in main.showing_records():

        hud.insert("" , 'end', values = (i[0], i[1], i[2], i[3]))

show()
display.mainloop()
