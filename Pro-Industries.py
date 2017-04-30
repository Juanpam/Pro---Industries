import test
import filesSupport as fs
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import machines
import winsound
import pronostics as pr
from PIL import ImageTk, Image

"""
Main module for the Pro-Industries Software.
"""
print(pr.findOptimalAlpha(pr.readData(fs.resource_path("csvTest.csv"))))

class Application(tk.Frame):

    title = "Pro-Industries Software"
    titleMod1 = title + " Módulo 1: Planeación agregada"
    titleMod2 = title + " Módulo 2: Plan Maestro de Producción"
    titleMod3 = title + " Módulo 3: Estructura de Producto"
    titleMod4 = title + " Módulo 4: Demanda y Combinación de Productos Óptima"
    iconPath = fs.resource_path("iconExe.ico")
    logoPath = fs.resource_path("Settings.png")
    autor1 = "Luis Ernesto Perafan Chacón"
    autor2 = "Sergio Cordoba"
    versionNumber = "1.0"

    def __init__(self, master=None):
        super().__init__(master)
        master.resizable(False,False)
        self.master.wm_title(self.title)
        self.master.iconbitmap(self.iconPath)
        self.master.minsize(400, 600)
        self.createWidgets()
        self.center(master)
        self.pack()

    def center(self,toplevel,dialog=False):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        if(dialog):
            y = h / 2 - size[1] / 2
        else:
            y = y - 40
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def createWidgets(self):
        # Welcome text
        self.hi_there = tk.Label(self, font="size 16")
        self.hi_there["text"] = "Bienvenido a\n" + self.title
        self.hi_there.pack(side="top")

        # Logotype loading
        img = Image.open(self.logoPath)
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.imgLabel = tk.Label(self, image=img)
        self.imgLabel.image = img
        self.imgLabel.pack(side="top")

        # Select module label
        self.selectOptionL = tk.Label(self, font="size 16", text="\n\nSeleccione un módulo:")
        self.selectOptionL.pack(side="top")

        # Create a separator
        ttk.Separator(self).pack(side="top", fill="both",pady=20)

        # Create Button Options
        self.button1 = tk.Button(
            self, text="Módulo 1:\nPlaneación agregada",
            command=lambda: self.initiateModule(1)).pack(
            side="top", fill="both", pady=10)
        self.button2 = tk.Button(
            self, text="Módulo 2:\nPlan Maestro de Producción",
            command=lambda: self.initiateModule(2)).pack(
            side="top", fill="both", pady=10)
        self.button3 = tk.Button(
            self, text="Módulo 3:\nEstructura de producto",
            command=lambda: self.initiateModule(3)).pack(
            side="top", fill="both", pady=10)
        self.button4 = tk.Button(
            self, text="Módulo 4:\nDemanda y Combinación de Productos Óptima",
            command=lambda: self.initiateModule(4)).pack(
            side="top", pady=10)

        # Menubar creation
        self.menubar = tk.Menu(self.master)
        self.menubar.add_command(label="Acerca de", background=self['background'],command=self.open_about)
        self.master.config(menu=self.menubar)

    def open_about(self):
        winsound.PlaySound(fs.resource_path('shingeki-no-kyojin-the-armored.wav'), winsound.SND_ALIAS | winsound.SND_ASYNC)
        tk.messagebox.showinfo("Acerca de","Desarrollado por:\n\n" + self.autor1 + "\n\ny\n\n" + self.autor2 + "\n\nVersión "+ self.versionNumber)
        winsound.PlaySound(None, winsound.SND_ALIAS | winsound.SND_ASYNC)

    def initiateModule(self,modNumber):
        if(modNumber == 1):
            height, width, title = 500, 500, self.titleMod1
        elif(modNumber == 2):
            height, width, title = 500, 500, self.titleMod2
        elif(modNumber == 3):
            height, width, title = 500, 500, self.titleMod3
        elif(modNumber == 4):
            height, width, title = 500, 700, self.titleMod4

        w = tk.Toplevel(self.master,height=height,width=width)
        w.title(title)
        w.iconbitmap(self.iconPath)
        w.withdraw()
        w.grab_set()
        w.focus_force()
        self.center(w,True)
        w.deiconify()
        self.master.withdraw()
        self.wait_window(w)
        self.master.deiconify()
        self.createModuleWidgets(w,modNumber)

    def createModuleWidgets(self, module, modNumber):
        if(modNumber==1):
            pass
        elif(modNumber==2):
            pass
        elif(modNumber==3):
            pass
        elif(modNumber==4):
            pass
        pass





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
