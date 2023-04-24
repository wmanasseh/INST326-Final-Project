import contacts

from tkinter import ttk

from tkinter import *



display = Tk()


display.geometry("800x700")


frame1 = Frame(display)

frame1.place (x = 50, y = 10)

frame2 = Frame(display)

frame2.place (x = 10, y = 10)




hud = ttk.Treeview(frame1, height=30)

hud.pack()



scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=hud.yview)

scrollbar.pack()


# Defining the number of columns
hud["columns"] = ("1", "2", "3", "4")

# Defining the headings
hud['show'] = 'headings'

# Assigning the width and anchor to the respective columns

hud.column ("1", width = 100, anchor ='c')

hud.column ("2", width = 210, anchor ='c')

hud.column ("3", width = 210, anchor ='c')

hud.column ("4", width = 210, anchor ='c')


# Assigning the heading names to the respective columns

hud.heading ("1", text = "ROW-ID")

hud.heading ("2", text = "First-Name")

hud.heading ("3", text = "Last-Name")

hud.heading ("4", text = "Phone-Number")




### We need to create the lables with the button names
### Our main problem is that we cant see the results of the code above.\
### We are not getting errors but we need to figure out how to test the code we have written




