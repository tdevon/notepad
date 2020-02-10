from tkinter import *

root = Tk()

sidebar = Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

for i in range(1,3):
    label = Label(sidebar, text="Item", width=15, height=1, anchor=NW, justify=LEFT)
    label.pack(fill=X)

mainarea = Frame(root, bg='#CCC', width=500, height=500)
mainarea.pack(expand=True, fill='both', side='right')

root.mainloop()