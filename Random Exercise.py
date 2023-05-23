# REG - Random Exercise Generator
# v1.07 Up to 2 exercises allowed at a time, Supersets on each day
# Changes added - external files used for lists

import tkinter as tk
from tkinter import *
import random
from time import sleep
from datetime import date, datetime

def openFile(group): #reads exercise files
    out = []
    str = "groups/" + group + ".txt"
    f = open(str,"r")
    for x in f:
        out.append(x.strip())
    return out

#set variables
chest = openFile("chest")
tri = openFile("tri")
back = openFile("back")
bi = openFile("bi")
legs = openFile("legs")
shoulders = openFile("shoulders")
core = openFile("core")
stretches = openFile("stretches")
comboDay = chest + tri + back + bi + legs + shoulders + core + stretches
groups = ["chest","tri","back","bi","legs","shoudlers","core","stretches"]
exerciseList = []
exerciseCount = 0

def addExercise(newGrp, newEx): #add a new exercise to the lists
    str = "groups/" + newGrp + ".txt"
    f = open(str,"a")
    f.write("\n" + newEx)
    f.close()

def resetExercises(): #resets the exercise list after new exercise is added
    global chest 
    global tri
    global back
    global bi
    global legs
    global shoulders
    global core
    global stretches
    global comboDay
    chest = openFile("chest")
    tri = openFile("tri")
    back = openFile("back")
    bi = openFile("bi")
    legs = openFile("legs")
    shoulders = openFile("shoulders")
    core = openFile("core")
    stretches = openFile("stretches")
    comboDay = chest + tri + back + bi + legs + shoulders + core + stretches

def monday(): #generates exercises for monday
    title = 'Today is Monday, that means it\'s Chest and Tri day.\nYour exercises are:\n'
    exercise1 = random.choice(chest)
    exercise2 = random.choice(tri)
    exercise3 = random.choice(chest)
    exercise4 = random.choice(tri)
    return title + "\n" + exercise1 + "\n&\n" + exercise2 + "\n&\n" + exercise3 + "\n&\n" + exercise4

def tuesday(): #generates exercises for tuesday
    title = 'Today is Tuesday, that means it\'s Back and Bi day.\nYour exercises are:\n'
    exercise1 = random.choice(back)
    exercise2 = random.choice(bi)
    exercise3 = random.choice(back)
    exercise4 = random.choice(bi)
    return title + "\n" + exercise1 + "\n&\n" + exercise2 + "\n&\n" + exercise3 + "\n&\n" + exercise4

def thursday(): #generates exercises for wednesday
    title = 'Today is Thursday, that means it\'s Legs and Shoulders day.\nYour exercises are:\n'
    exercise1 = random.choice(legs)
    exercise2 = random.choice(shoulders)
    exercise3 = random.choice(legs)
    exercise4 = random.choice(shoulders)
    return title + "\n" + exercise1 + "\n&\n" + exercise2 + "\n&\n" + exercise3 + "\n&\n" + exercise4

def wednesday(): #generates exercises for thursday
    title = 'Today is Wednesday, that means it\'s Core and Stretches day.\nYour exercises are:\n'
    exercise1 = random.choice(core)
    exercise2 = random.choice(stretches)
    exercise3 = random.choice(core)
    exercise4 = random.choice(stretches)
    return title + "\n" + exercise1 + "\n&\n" + exercise2 + "\n&\n" + exercise3 + "\n&\n" + exercise4

def friday(): #generates exercises for friday
    title = 'Today is Friday, that means it\'s Combo day.\nYour exercises are:\n'
    exercise1 = random.choice(comboDay)
    exercise2 = random.choice(comboDay)
    exercise3 = random.choice(comboDay)
    exercise4 = random.choice(comboDay)
    return title + "\n" + exercise1 + "\n&\n" + exercise2 + "\n&\n" + exercise3 + "\n&\n" + exercise4

def day(): #returns exercise list depending on day of the week
    if date.today().weekday() == 0:
        return monday()
    elif date.today().weekday() == 1:
        return tuesday()
    elif date.today().weekday() == 2:
        return wednesday()
    elif date.today().weekday() == 3:
        return thursday()
    elif date.today().weekday() == 4:
        return friday()
    
def dailyExercise(): #returns exercise group names for the day
    if date.today().weekday() == 0:
        return chest + [""] + tri
    elif date.today().weekday() == 1:
        return back + [""] + bi
    elif date.today().weekday() == 2:
        return core + [""] +  stretches
    elif date.today().weekday() == 3:
        return legs + [""] +  shoulders
    elif date.today().weekday() == 4:
        return comboDay

def inputWindow(): #runs window to input new exercise
    
    def submit():
        grp = groupEntry.get()
        ex = exEntry.get()
        if grp not in groups:
            warning_var.set("Not in groups list")
            warning.config(fg="red", font = ('calibre',12,'normal'))
        else:
            addExercise(grp, ex)
            warning_var.set("Exercise Added Succesfully\nFeel free to add more")
            warning.config(fg="black", font = ('calibre', 10, 'normal'))
            newExGroup_var.set("")
            groupEntry.delete(0,END)
            exEntry.delete(0,END)
            resetExercises()

    root2 = tk.Tk()
    root2.title("New workout")
    root2.geometry("240x200")
    root2.after(1, lambda: root2.focus_force())
    
    warning_var = StringVar(root2, "")
    newExGroup_var = tk.StringVar()
    newExercise_var = tk.StringVar()
    
    titleVar = tk.Label(root2, text = "=====Enter the new exercise below=====")
    newExGroup = tk.Label(root2, text = "New Group:")
    groupEntry = tk.Entry(root2, textvariable=newExGroup_var)
    newEx = tk.Label(root2, text = "New exercise:")
    exEntry = tk.Entry(root2, textvariable=newExercise_var)
    sub_btn = tk.Button(root2, text = "Submit", command = submit)
    exit_btn = tk.Button(root2, text = "Quit", command=root2.destroy)
    warning = tk.Label(root2, textvariable=warning_var)

    titleVar.grid(row=0,column=1)
    newExGroup.grid(row=1,column=1)
    groupEntry.grid(row=2,column=1)
    newEx.grid(row=4,column=1)
    exEntry.grid(row=5,column=1)
    sub_btn.grid(row=6,column=1)
    exit_btn.grid(row=8,column=1)
    warning.grid(row=7,column=1)
    groupEntry.focus()

    root2.mainloop()

def mainwindow(): # runs main window
    def change():  # changed the Random Exercise, maximum of 2 exercises
        global exerciseCount
        exerciseCount = exerciseCount + 1
        if exerciseCount >= 2:
            var.set('That\'s enough for now')
        else:
            var.set(day())

    def show():  # Show the list of exercises and resets exercise count
        global exerciseCount
        exerciseCount = -1  # set to -1 to allow 2 more choices
        out= "\n"
        today = dailyExercise()
        for i in today:
            out = out + i + "\n"
        var.set("Today's exercise list: " + "\n" + out)
    
    def addExercise():
        inputWindow()

    root = Tk()
    var = StringVar()
    var.set(day())
    repeatCheck = StringVar()
    repeatCheck.set(var)  # First attempt to make it not repeat exercises, need to create a reduced list once one has been used
    #print(repeatCheck)
    #print(exerciseList)

    frame_a = tk.Frame(master=root, width=200, height=100)
    frame_b = tk.Frame(master=root, width=200, height=50)
    title = tk.Label(master=frame_a, text="===========Random Exercise Generator v1.07 ===========\n\n")
    randomlabel = tk.Label(master=frame_a, textvariable=var)
    exitline = tk.Label(master=frame_a, text="\nWould you like to do more?\n")

    btn_quit = tk.Button(
        master=frame_b,
        text="Quit",
        width=15,
        height=5,
        bg='white',
        fg='black',
        command=exit
    )
    btn_new = tk.Button(
        master=frame_b,
        text="New Exercise",
        width=15,
        height=5,
        bg='white',
        fg='black',
        command=change
    )
    btn_add = tk.Button(
        master=frame_b,
        text="Add Exercise",
        width=15,
        height=2,
        bg='white',
        fg='black',
        command=addExercise
    )
    btn_show = tk.Button(
        master=frame_b,
        text="Show Exercise List",
        width=15,
        height=2,
        bg='white',
        fg='black',
        command=show
    )
    frame_a.pack(expand=False)
    frame_b.pack(expand=True)
    title.pack()
    randomlabel.pack()
    exitline.pack()
    btn_new.grid(row=0, column=1, padx=1, pady=5)
    btn_add.grid(row=-0, column=2, sticky='N', padx=1, pady=5)
    btn_show.grid(row=0, column=2, sticky='S', padx=1, pady=5)
    btn_quit.grid(row=0, column=3, padx=1, pady=5)

    root.mainloop()

mainwindow()  # Runs main window


