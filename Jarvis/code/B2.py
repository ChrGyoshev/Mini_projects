from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import math
import os
import sys


def calc(a):
    file = open("sample.txt", "r")
    dataint = file.readline()
    dataint = float(dataint) + a
    file.close()
    file = open("sample.txt", "w")
    file.write(str(dataint))
    file.close()
    e.delete(0, END)
    result = f'{dataint:.1f}'
    e.insert(0, result)


def clr():
    # save to log file
    file = open("sample.txt", "r")
    dataint_one = file.readline()
    dataint_one = float(dataint_one)
    dataint_one = f'{dataint_one:.1f}'
    log_file = open('log.txt', 'a')
    log_file.write(str(dataint_one))
    log_file.write("\n")

    # save to sample file
    file = open("sample.txt", "w")
    file.write(str(0))
    file.close()
    e.delete(0, END)
    file = open("sample.txt", "r")
    data = file.readline()
    file.close()
    e.insert(0, data)


# Change buttons_light_functions
def change_1(e):
    my_pic = button_one_light_img
    button1.config(image=my_pic)
    button1.image = my_pic


def change_back_1(e):
    my_pic = button_one_light_img
    button1.config(image=button_one_img)
    button1.image = my_pic


def change_2(e):
    my_pic = button_two_light_img
    button2.config(image=my_pic)
    button2.image = my_pic


def change_back_2(e):
    my_pic = button_two_light_img
    button2.config(image=button_two_img)
    button2.image = my_pic


def change_3(e):
    my_pic = button_three_light_img
    button3.config(image=my_pic)
    button3.image = my_pic


def change_back_3(e):
    my_pic = button_three_light_img
    button3.config(image=button_three_img)
    button3.image = my_pic


def change_4(e):
    my_pic = button_four_light_img
    button4.config(image=my_pic)
    button4.image = my_pic


def change_back_4(e):
    my_pic = button_four_light_img
    button4.config(image=button_four_img)
    button4.image = my_pic


def change_5(e):
    my_pic = button_five_light_img
    button5.config(image=my_pic)
    button5.image = my_pic


def change_back_5(e):
    my_pic = button_five_light_img
    button5.config(image=button_five_img)
    button5.image = my_pic


def change_6(e):
    my_pic = button_six_light_img
    button_clr.config(image=my_pic)
    button_clr.image = my_pic


def change_6_back(e):
    global button_clr
    my_pic = button_six_light_img
    button_clr.config(image=button_six_img)
    button_clr.image = my_pic


# Resource
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Window
back = resource_path("picture.png")
window = Tk()
window.title("Jarvis")

# win center
app_width = 300
app_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
window.resizable(width=False, height=False)

icon = resource_path("iconn.ico")
window.iconbitmap(icon)

# background
canv = Canvas(window, width=300, height=400, bd=0, highlightthickness=0, relief='ridge')
canv.pack()

img = ImageTk.PhotoImage(Image.open(back))  # PIL solution
canv.create_image(0, 0, anchor=NW, image=img)

# button_img
# 1
button_one = resource_path("button_1.png")
button_one_img = ImageTk.PhotoImage(Image.open(button_one))
# 2
button_two = resource_path("button_2.png")
button_two_img = ImageTk.PhotoImage(Image.open(button_two))
# 3
button_three = resource_path("button_3.png")
button_three_img = ImageTk.PhotoImage(Image.open(button_three))
# 4
button_four = resource_path("button_4.png")
button_four_img = ImageTk.PhotoImage(Image.open(button_four))
# 5
button_five = resource_path("button_5.png")
button_five_img = ImageTk.PhotoImage(Image.open(button_five))
# 6
button_six = resource_path("button_6.png")
button_six_img = ImageTk.PhotoImage(Image.open(button_six))

# Buttons_lights
# 1 -70brightness
button_one_light = resource_path("button_1_light.png")
button_one_light_img = ImageTk.PhotoImage(Image.open(button_one_light))
# 2
button_two_light = resource_path("button_2_light.png")
button_two_light_img = ImageTk.PhotoImage(Image.open(button_two_light))
# 3
button_three_light = resource_path("button_3_light.png")
button_three_light_img = ImageTk.PhotoImage(Image.open(button_three_light))
# 4
button_four_light = resource_path("button_4_light.png")
button_four_light_img = ImageTk.PhotoImage(Image.open(button_four_light))
# 5
button_five_light = resource_path("button_5_light.png")
button_five_light_img = ImageTk.PhotoImage(Image.open(button_five_light))
# 6
button_six_light = resource_path("button_6_light.png")
button_six_light_img = ImageTk.PhotoImage(Image.open(button_six_light))

# entry
e = Entry(window, width=19, borderwidth=5, bg="#e7c5b0", font=('Arial', 14))
e_window = canv.create_window(40, 10, anchor='nw', window=e)
# entry_summar
e_sum = Entry(window, width=5, borderwidth=5, font=("Arial", 12), bg="#13333e", fg="white")
e_sum_window = canv.create_window(235, 260, anchor="nw", window=e_sum)
file = open("sample.txt", "r")
dataint_one = file.readline()
dataint_one = float(dataint_one)
dataint_one = f'{dataint_one:.1f}'
e.insert(0, dataint_one)

# display_summing
myfile = "log.txt"
fh = open(myfile, "r")
sum = 0
for n in fh:
    n = n.strip()
    sum = sum + float(n)
    result = f'{sum:.1f}'
fh.close()

e_sum.insert(0, result)

# Display Buttons
button1 = Button(canv, image=button_one_img, command=lambda: calc(0.1), bd=0, width=62, height=33, cursor="hand2")
button1.bind("<Enter>", change_1)
button1.bind("<Leave>", change_back_1)
button1_window = canv.create_window(35, 80, anchor="nw", window=button1)

# button_2
button2 = Button(canv, image=button_two_img, command=lambda: calc(0.2), bd=0, width=62, height=33, cursor='hand2')
button2.bind("<Enter>", change_2)
button2.bind("<Leave>", change_back_2)
button2_window = canv.create_window(120, 80, anchor="nw", window=button2)

# button_3
button3 = Button(canv, image=button_three_img, command=lambda: calc(0.4), bd=0, width=62, height=33, cursor='hand2')
button3.bind("<Enter>", change_3)
button3.bind("<Leave>", change_back_3)
button3_window = canv.create_window(200, 80, anchor="nw", window=button3)

# button_4
button4 = Button(canv, image=button_four_img, command=lambda: calc(0.8), bd=0, width=62, height=33, cursor='hand2')
button4.bind("<Enter>", change_4)
button4.bind("<Leave>", change_back_4)
button4_window = canv.create_window(35, 150, anchor="nw", window=button4)

# button_5
button5 = Button(canv, image=button_five_img, command=lambda: calc(1.2), bd=0, width=62, height=33, cursor='hand2')
button5.bind("<Enter>", change_5)
button5.bind("<Leave>", change_back_5)
button5_window = canv.create_window(120, 150, anchor="nw", window=button5)

# button_clear
button_clr = Button(canv, image=button_six_img, command=lambda: clr(), bd=0, width=62, height=33, cursor='hand2')
button_clr.bind("<Enter>", change_6)
button_clr.bind("<Leave>", change_6_back)
button_clr_window = canv.create_window(200, 150, anchor="nw", window=button_clr)

window.mainloop()
