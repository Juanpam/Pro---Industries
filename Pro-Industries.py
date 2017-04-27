import sys
import os
import tkinter as tk
from PIL import ImageTk, Image

"""
Developed by Juan Pablo Méndez
Main module for the Pro-Industries Software.
"""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Application(tk.Frame):

    title = "Pro-Industries Software"
    iconPath = resource_path("iconExe.ico")
    logoPath = resource_path("Settings.png")

    def __init__(self, master=None):
        super().__init__(master)
        self.master.wm_title(self.title)
        self.master.iconbitmap(self.iconPath)
        self.master.minsize(500, 500)
        self.center(master)
        self.pack()
        self.create_widgets()

    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def create_widgets(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = "Bienvenido a\n" + self.title
        self.hi_there.pack(side="top")
        img = Image.open(self.logoPath)
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.button = tk.Label(self, image=img)
        self.button.image = img
        self.button.pack(side="top")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import os

# root = Tk()
# root.geometry("550x300+300+150")
# root.resizable(width=True, height=True)

# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = openfn()
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()

# btn = Button(root, text='open image', command=open_img).pack()

# root.mainloop()
