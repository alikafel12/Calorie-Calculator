# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 19:19:08 2018

@author: Ali Kafel
"""

from tkinter import *


def click():
    cal_output.delete(0.0, END)
    mac_output.delete(0.0, END)

    age = float(age_entry.get())

    weight = float(weight_entry.get())
    wunit = default_weight.get()
    if wunit == "lbs":
        weightkg = weight/2.2
        weightlb = weight
    else:
        weightkg = weight
        weightlb = weight * 2.2

    height = float(height_entry.get())
    hunit = default_height.get()
    if hunit == "inch":
        height = height * 2.54
    else:
        height = height

    act_level = default_level.get()

    ree = (10 * weightkg) + (6.25 * height) - (5 * age) + 5

    if act_level == "Sedentary":
        act_level = 1.2
    elif act_level == "Lightly Active":
        act_level = 1.375
    elif act_level == "Moderately Active":
        act_level = 1.55
    elif act_level == "Very Active":
        act_level = 1.725
    elif act_level == "Extremely Active":
        act_level = 1.9

    tdee = float(ree) * act_level
    calories = int(tdee * .80)
    cal_output.insert(END, calories)

    protein = str(int(.95 * weightlb)) + " " + "g protein\n"
    pcal = (.95 * weightlb) * 4
    fat = str(int((tdee * .25) / 9)) + " " + "g fat\n"
    fcal = ((tdee * .25)/9) * 9
    carbs = str(int((calories - (pcal + fcal)) / 4)) + " " + "g carbs\n"
    fiber = str(int(14 * (calories/1000))) + " " + "g fiber\n"
    mac_output.insert(END, protein, "", fat, "", carbs, "", fiber)


window = Tk()

window.title("Calories")
window.configure(background="white")
window.resizable(width=FALSE, height=FALSE)

# Labels
Label(window, text="Age", bg="white", fg="black", font="times 12").grid(row=0, column=0, sticky=W)
Label(window, text="Weight", bg="white", fg="black", font="times 12").grid(row=1, column=0, sticky=W)
Label(window, text="Height", bg="white", fg="black", font="times 12").grid(row=2, column=0, sticky=W)
Label(window, text="Activity Level", bg="white", fg="black", font="times 12").grid(row=3, column=0, sticky=W)
Label(window, text="Calories", bg="white", fg="black", font="times 12").grid(row=4, column=0, sticky=W)
Label(window, text="Macros", bg="white", fg="black", font="times 12").grid(row=5, column=0, sticky=W)

# Text Entries
age_entry = Entry(window, width=10, bg="white")
age_entry.grid(row=0, column=1, sticky=W)
weight_entry = Entry(window, width=10, bg="white")
weight_entry.grid(row=1, column=1, sticky=W)
height_entry = Entry(window, width=10, bg="white")
height_entry.grid(row=2, column=1, sticky=W)

# Button
Button(window, text="Submit", width=6, command=click).grid(row=7, column=5, sticky=W)

# Text Boxes
cal_output = Text(window, width=8, height=1, wrap=WORD, bg="white")
cal_output.grid(row=4, column=1, columnspan=2, sticky=W)
mac_output = Text(window, width=16, height=5, wrap=WORD, bg="white")
mac_output.grid(row=5, column=1, columnspan=2, sticky=W)

# Option Menus
activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]
default_level = StringVar()
default_level.set(activity_levels[0])
act_menu = OptionMenu(window, default_level, *activity_levels)
act_menu.grid(row=3, column=1, sticky=W)
weight_units = ["lbs", "kg"]
default_weight = StringVar()
default_weight.set(weight_units[0])
weight_menu = OptionMenu(window, default_weight, *weight_units)
weight_menu.grid(row=1, column=2, sticky=W)
height_units = ["inch", "cm"]
default_height = StringVar()
default_height.set(height_units[0])
height_menu = OptionMenu(window, default_height, *height_units)
height_menu.grid(row=2, column=2, sticky=W)

window.mainloop()
