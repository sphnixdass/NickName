import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import collections
import numpy as np

#pip install tkcalendar

root = tk.Tk()
root.geometry("500x600+30+30")
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()

def mainfun():
    print(v1.get())
    print(v2.get())
    print(v3.get())
    full_name(v1.get(), root)




def full_name(nickname, root):
    global Lb1
    with open("nicknames.db", 'r') as fin:
        lines = fin.readlines()
        # remove '\n' characters
        clean_lines = [l.strip('\n') for l in lines]
        # split on tab so that we get lists from strings
        A = [cl.split('\t') for cl in clean_lines]
        Lb1.delete(0,tk.END)
        Lb1.insert(1, nickname)
        for item in A:
            if item[0].lower() == nickname.lower():
                print(item[1])
                Lb1.insert(1, item[1].lower())

        # get lists of ints instead of lists of strings
        #X = [map(int, row[0:6]) for row in A]
        # last column in Y
        #Y = [row[6] for row in A]

        # convert string to int values
        #for i in xrange(len(Y)):
            #Y[i] = map(int, Y[i].strip('[]').split(','))



    # names = load_names()
    # for item in names:
    #     print(item[0])
    # print(len(names))
    #return names[nickname][weighted_choice_sub([x[1] for x in names[nickname]])][0]

w = tk.Label(root, text="Nick Name", bg="blue", fg="white")
w.place(x = 20, y = 50, width=120, height=25)
e1 = tk.Entry(root,textvariable=v1)
e1.place(x = 150, y = 50, width=200, height=25)
#w.pack(padx=5, pady=10, side=tk.LEFT)
w = tk.Label(root, text="Date of Birth", bg="blue", fg="white")
w.place(x = 20, y = 100, width=120, height=25)
cal = DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2, year=2010,textvariable=v2)
cal.place(x = 150, y = 100, width=120, height=25)

w = tk.Label(root, text="Postal Code", bg="blue", fg="white")
w.place(x = 20, y = 150, width=120, height=25)
e2 = tk.Entry(root,textvariable=v3)
e2.place(x = 150, y = 150, width=120, height=25)

w = tk.Button(root, text='Submit', command=mainfun)
w.place(x = 20, y = 200, width=120, height=25)

w = tk.Label(root, text="Artificial Intelligence Suggestions", bg="red", fg="white")
w.place(x = 20, y = 250, width=300, height=25)


Lb1 = tk.Listbox(root)
Lb1.place(x = 20, y = 300, width=150, height=200)


tk.mainloop()
