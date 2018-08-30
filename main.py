from tkinter import *

rt = Tk()
rt.title("InterPlanner 2018 [v0.2]")

name = Frame(rt)  # very top
name.pack(side=TOP)


Label(rt, text="My School Planner", font=("arial", 40)).pack(in_=name)
Label(rt, text="Date", font=("arial", 30)).pack(in_=name)

ind = 0
def inc():
    global ind
    ind += 1
    if ind >= len(color): ind = 0
    stat['bg'] = color[ind]
    stat['text'] = b_text[ind]

def assign():
    global work
    sub = input("SUB: ")
    works = input("HW: ")
    work.append([sub, works])
    rt.after(1, button())
    print(work)

color = ["#aaaaaa","#ffaa00","#00ff00", "#ff0000"]
b_text = ["Unbegun", "Partially", "Done", "Overdue"]
work = [["Subject", "Assigment"]]

add = Button(rt, text="+", font=("arial", 20), command=lambda: assign())
add.pack()

def button():
    print(work)
    for (subj, hw) in work:
        global stat
        planner = Frame(rt)
        planner.pack(side=TOP)
        Label(rt, text=subj, font=("arial", 20)).pack(in_=planner, side=LEFT)
        stat = Button(rt, text=b_text[ind], font=("arial", 20), command=lambda: inc(), bg=color[ind])
        stat.pack(in_=planner, side=LEFT)
        Label(rt, text=hw, font=("arial", 20)).pack(in_=planner, side=LEFT)

button()

rt.mainloop()
