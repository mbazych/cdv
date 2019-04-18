import sys
import os
from tkinter import *
import tkinter.filedialog as filedialog
def edit():
    root=Tk("Text Editor")
    text = Text(root)
    root.geometry("500x600")
    text.grid()


    def saveas():
        global text

        t = text.get("1.0", "end-1c")
        savelocation = filedialog.asksaveasfilename()
        file1        = open(savelocation, "w+")
        file1.write(t)
        file1.close()

    def open_file(event=None):
        input_file_name = filedialog.askopenfilename()
        if input_file_name:
            global file_name
            file_name = input_file_name
            text.delete(1.0, END)
            with open(file_name) as _file:
                text.insert(1.0, _file.read())

    button = Button(root, text="Save", command = saveas)
    opens = Button(root, text="Open", command = open_file)
    button.place(x=240, y=575)
    opens.place(x=238, y=550)

    def FontHelvetica():
        global text

        text.config(font="Helvetica")

    def FontCourier():
        global text

        text.config(font="Courier")


    font = Menubutton(root, text="Font")
    font.menu = Menu(font, tearoff=0)
    font["menu"] = font.menu
    font.place(x=240, y=525)

    helvetica   =IntVar()
    courier     =IntVar()

    font.menu.add_checkbutton(label="Courier", variable=courier, command = FontCourier)
    font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command = FontHelvetica)
    root.mainloop()
