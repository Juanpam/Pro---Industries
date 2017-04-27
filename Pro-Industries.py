import sys
import os
import tkinter as tk
import tkinter.messagebox
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
    autor1 = "Luis Ernesto Perafan Chacón"
    autor2 = "Sergio Cordoba"
    versionNumber = "1.0"

    def __init__(self, master=None):
        super().__init__(master)
        master.resizable(False,False)
        self.master.wm_title(self.title)
        self.master.iconbitmap(self.iconPath)
        self.master.minsize(400, 600)
        self.create_widgets()
        self.center(master)
        self.pack()

    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = 0
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def create_widgets(self):
    	#Welcome text
        self.hi_there = tk.Label(self,font="size 16")
        self.hi_there["text"] = "Bienvenido a\n" + self.title
        self.hi_there.pack(side="top")

        #Logotype loading
        img = Image.open(self.logoPath)
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.imgLabel = tk.Label(self, image=img)
        self.imgLabel.image = img
        self.imgLabel.pack(side="top")
        self.selectOptionL = tk.Label(self, font="size 16", text="\n\nSeleccione un módulo:")
        self.selectOptionL.pack(side="top")
        top = self.winfo_toplevel()
        self.menubar = tk.Menu(self.master)
        self.menubar.add_command(label="Acerca", background=self['background'],command=self.open_about)
        self.master.config(menu=self.menubar)

    def open_about(self):
    	tk.messagebox.showinfo("Acerca de","Desarrollado por:\n\n" + self.autor1 + "\n\ny\n\n" + self.autor2 + "\n\nVersión "+ self.versionNumber)







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
