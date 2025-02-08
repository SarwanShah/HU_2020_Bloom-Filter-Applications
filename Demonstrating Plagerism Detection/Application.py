import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from array import *
from filterFileHandler import *
from BloomFilter import BloomFilter

# Globals
# array1 = ["a", "b", "c", "d"]

# Function call to generate Bloom Filter
res = loadFilterFile('MainFilterFile-1001-1-7-9600.txt')
# print(res.getBitArray())
# lst.loadFilter('Filter1.txt', 7, 0.01)
# Function to check if file exists in dataset

# Filter = BloomFilter()
# file = open('testData1.txt')
# Filter.generateEmptyFilter(1001, 0.01)
# for line in file:
#     Filter.add(line[:40])

# print(Filter.check("7C4A8D09CA3762AF61E59520943DC26494F8941B"))


def verify(inp):
    if res.check(inp):
        # if res.check("7C4A8D09CA3762AF61E59520943DC26494F8941B:23597311"):
        # Placeholder. Check for valid in an array. Replace this with Search function of Bloomfilter
        return True
    else:
        return False


def clickGetResults():  # Event handler for click on Search in main menu
    userInput = userInputTextBox.get()  # gets text written in text box
    userInputTextBox.delete(0, END)  # erases the text box
    #    print(userInput)
    Results = tk.Toplevel()  # Creates a window on TOP of previous window

    w = 500
    h = 100
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    Results.geometry("%dx%d+%d+%d" % (w, h, x, y))  # sets the size of the
    Results.grab_set()  # disbales interaction with previous windon untill this one is closed

    if verify(userInput):
        Results.title("true")
        tk.Label(Results, text="Your password is compromised.").grid(
            row=0, column=0, sticky=W
        )

    else:
        Results.title("false")
        tk.Label(Results, text="Your password is safe.").grid(
            row=0, column=0, sticky=W)


# Main
Root = tk.Tk()
Root.title("Password Check")
picSkull = PhotoImage(file="background.png")
tk.Label(Root, image=picSkull, bg="black").grid(row=0, column=0, sticky=E)
Root.configure(background="black")
Root.resizable(0, 0)  # fixes size

# get screen width and height
ws = Root.winfo_screenwidth()  # width of the screen
hs = Root.winfo_screenheight()  # height of the screen

tk.Label(
    Root,
    text="Enter the password to check for hacks and leaks:",
    bg="black",
    fg="white",
    font=("Times New Roman", 18),
).grid(row=1, column=0, sticky=W + E)

userInputTextBox = Entry(Root, width=36, bg="white")
userInputTextBox.grid(row=2, column=0, sticky=N)
tk.Label(Root, bg="black").grid(row=3)
tk.Button(Root, text="Search!", width=30, command=clickGetResults).grid(
    row=4, column=0, sticky=N
)

Root.eval("tk::PlaceWindow . center")

Root.mainloop()
