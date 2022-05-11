#Def_submit_button:
def submit():
    while True:
        if data_2.get() < data_1.get():
            from tkinter import messagebox
            messagebox.showerror("Wrong data", "Invalid data entered: Try again!")
            break
        else:
            calculation = (data_2.get() - data_1.get()) / data_3.get()
            empty_label.config(text="You need " + f'{math.ceil(calculation)}' " more games to level up.  ", font=('Calibri', 14))
            empty_label.grid(row =5, column = 0, padx = 18, pady = 0, sticky="",columnspan = 2)
            break
def exit_button():
    window.destroy()

from tkinter import *
from turtle import width
from PIL import Image, ImageTk
import math
import sys
import os


# Import .ico and images:
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#Define resources:
icon = resource_path("diablo_logo.ico")
logo = resource_path("diablo.png")


#Define window:
window = Tk()
window.title("Diablo II ressurected XP Calculator")
window.iconbitmap(icon)

window.eval('tk::PlaceWindow . center')

Grid.rowconfigure(window,0, weight= 1)
Grid.columnconfigure(window,0, weight=1)

Grid.columnconfigure(window,1, weight=1)
Grid.columnconfigure(window,2, weight=1)
Grid.columnconfigure(window,3, weight=1)
Grid.columnconfigure(window,6, weight=1)


#Logo_insert:
logo = Image.open(logo)
resized_logo= logo.resize((300,180), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)
label = Label(image = new_logo)
label.image = new_logo
label.grid(row = 0, column = 0, padx=0, pady=0, sticky="", columnspan = 3)

#Current_xp:
    #text:
current_xp = Label(window, text='Enter current XP: ', font=("Calibri", 11, "bold"))
current_xp.grid(row =1, column= 0, padx=10, pady=0, sticky="W",)
    #entry_box:
data_1 = DoubleVar()
current_xp_box =Entry(window, textvariable= data_1, width= 20, borderwidth=3)
current_xp_box.grid(row=1, column=1, padx=0, pady=3, sticky='')
current_xp_box.delete(0,END)

#Next_xp:
next_xp = Label(window, text="Enter Xp needed to next level: ", font=("Calibri", 11, "bold"))
next_xp.grid(row=2, column=0, padx=10, pady=0, sticky="W")
    #entry_box:
data_2 = DoubleVar()
next_xp_box = Entry(window, textvariable= data_2, width=20, borderwidth=3)
next_xp_box.grid(row=2, column=1, padx=30, pady=3, sticky="")
next_xp_box.delete(0, END)

#step:
step = Label(window, text="Enter current XP per game: ", font=("Calibri", 11, "bold"))
step.grid(row=3, column=0, padx=10, pady=0, sticky="W")
    #entry_box:
data_3 = DoubleVar()
step_box = Entry(window, textvariable= data_3, width=20, borderwidth=3)
step_box.grid(row=3, column =1, padx=5, pady= 3, sticky = "" )
step_box.delete(0,END)


#Result:
empty_label = Label(window, font=("Calibri", 11, "bold",),fg = "green")
empty_label.grid(row=4, column=0,padx=5, pady=0, sticky="")



#Buttons:
submit_button=Button(window,command=submit, text="Submit", font=("Calibri", 11, "bold"), borderwidth=4, width=9, activeforeground="#083C04")
submit_button.grid(row=6, column=1, padx=0, pady=10, sticky="")

exit_button = Button(window, command=exit_button, text="Exit", font=("Calibri", 11, "bold"), borderwidth=4, width=9, activeforeground="#083C04")
exit_button.grid(row=6, column = 0, padx=0, pady=0 , sticky="")


window.mainloop()

