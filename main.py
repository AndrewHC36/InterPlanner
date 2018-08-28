from tkinter import *

rt = Tk()
rt.title("InterPlanner 2018 v1.0")
rt.geometry("1920x1080")

title = Label(rt, text="My School Planner", font=("arial", 20))
title.pack()

planner = [["8-26-2018 - Sun", ["Music", "Done", "Finish work sheet #3-5"]]]

section_date = Label(rt, text="{}/{}/{} - {}".format(8, 26, 2018, "Sun"), font=("arial", 15))
section_date.pack()

subj = Label(rt, text=planner[0][1][0], font=("arial", 20))
stat = Button(rt, text=planner[0][1][1], font=("arial", 20))
assign = Label(rt, text=planner[0][1][2], font=("arial", 20))

subj.pack(side=LEFT, anchor="n")
stat.pack(side=LEFT, anchor="n")
assign.pack(side=LEFT, anchor="n")
rt.mainloop()