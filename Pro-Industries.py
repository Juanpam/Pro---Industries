import test
import filesSupport as fs
import machines
import winsound
import pronostics as pr
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

from PIL import ImageTk, Image

"""
Main module for the Pro-Industries Software.
"""
#pr.genGraph(pr.readData(fs.resource_path("csvTest.csv")))

class Application(tk.Frame):

    title = "Pro-Industries Software"
    titleMod1 = " Módulo 1: Planeación agregada"
    titleMod2 = " Módulo 2: Pronóstico de Demanda"
    titleMod3 = " Módulo 3: Estructura de Producto"
    titleMod4 = " Módulo 4: Demanda y Combinación de Productos Óptima"
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
            self, text="Módulo 2:\nPronóstico de Demanda",
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
            height, width, title = 400, 400, self.titleMod2
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
        module(w, height, width, title, modNumber)
        w.deiconify()
        self.master.withdraw()
        self.wait_window(w)
        self.master.deiconify()


class module (tk.Frame):
    """
    Base class for a module
    """
    center = Application.center
    iconPath = fs.resource_path("iconExe.ico")
    filePath = None

    def __init__(self, master, height, width, title, modNumber):
        super().__init__(master)
        #master.resizable(False,False)
        self.master.wm_title(title)
        self.master.iconbitmap(self.iconPath)
        self.createWidgets(modNumber)
        self.center(master,True)
        self.pack(fill="both",expand=True)

    def createWidgets(self, modNumber):
        """
        Sets-up the widgets according to each module
        """
        if(modNumber==1):
            pass
        elif(modNumber==2):
            #Creacion de widgets para el segundo módulo



            #Dynamic variable for the filename
            self.fileName = tk.StringVar(value="Nombre de archivo: ")
            if(self.filePath):
                self.fileName.set(fileName.get() + fs.baseName(self.filePath))
            else:
                self.fileName.set("Cargue un archivo porfavor.")
            nameLabel = tk.Label(self,textvariable=self.fileName)
            self.columnconfigure(0,weight=1)
            self.columnconfigure(1,weight=1)
            self.rowconfigure(0,weight=1)
            for i in range(1,10):
                self.rowconfigure(i,weight=1)
            nameLabel.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S,columnspan=2,rowspan=2)


            loadData = tk.Button(
            self, text="Cargar datos históricos",
            command = lambda : self.openFile())
            loadData.grid(row=2,sticky=tk.W+tk.E+tk.S+tk.N)

            
            genPronostic = tk.Button(
            self, text="Graficar pronostico",
            command=lambda : self.genGraph(self.filePath))
            genPronostic.grid(row=2,column=1,sticky=tk.W+tk.E+tk.N+tk.S)

            doPronostic = tk.Button(
            self, text="Calcular Variables",
            command=lambda : self.doPronostic(self.filePath))
            doPronostic.grid(row=3,column=1,sticky=tk.W+tk.E+tk.N+tk.S)


            optAlpha = tk.Button(
            self, text="Obtener Alpha óptimo",
            command=lambda : self.getOptAlpha(self.filePath))
            optAlpha.grid(row=3,column=0,sticky=tk.W+tk.E+tk.N+tk.S)

            #Weeks entry
            tk.Label(self,text="Semanas de historico: ").grid(row=4, column=0)
            self.weeks = tk.IntVar(value=12)
            tk.Entry(self,textvariable=self.weeks).grid(row=4, column=1,sticky=tk.W+tk.E)

            #Alpha entry
            tk.Label(self,text="Valor de alpha: ").grid(row=5, column=0)
            self.alpha = tk.DoubleVar(value=0.5)
            tk.Entry(self,textvariable=self.alpha).grid(row=5, column=1,sticky=tk.W+tk.E)

            #MAPE
            tk.Label(self,text="MAPE: ").grid(row=6, column=0)
            self.MAPE = tk.DoubleVar()
            tk.Label(self,textvariable=self.MAPE).grid(row=6, column=1,sticky=tk.W+tk.E)

            #ECM

            tk.Label(self,text="ECM: ").grid(row=7, column=0)
            self.ECM = tk.DoubleVar()
            tk.Label(self,textvariable=self.ECM).grid(row=7, column=1,sticky=tk.W+tk.E)

            #SD

            tk.Label(self,text="Desviación estandar: ").grid(row=8, column=0)
            self.SD = tk.DoubleVar()
            tk.Label(self,textvariable=self.SD).grid(row=8, column=1,sticky=tk.W+tk.E)

            #CVD

            tk.Label(self,text="CVD: ").grid(row=9, column=0)
            self.CVD = tk.DoubleVar()
            tk.Label(self,textvariable=self.CVD).grid(row=9, column=1,sticky=tk.W+tk.E)
            

        elif(modNumber==3):
            pass
        elif(modNumber==4):

            #Conf of expansion
            self.columnconfigure(0,weight=1,pad=20)
            self.columnconfigure(1,weight=1,pad=20)
            #self.rowconfigure(0,weight=1,pad=400)

            #Product
            addProductButton = tk.Button(
            self, text="Seleccione un producto: ",command=lambda : combo.configure(values=combo.cget("values")+("extra",)))
            addProductButton.grid(row=0,sticky=tk.N+tk.E+tk.S+tk.W)
            stringVar = tk.StringVar()
            values=["Agregar producto..."]
            combo = ttk.Combobox(self,textvariable=stringVar,state='readonly')
            combo['values']=values
            combo.grid(row=0,column=1,sticky=tk.N+tk.E+tk.S+tk.W)
            combo.bind('<<ComboboxSelected>>', lambda x : self.funcioncita(combo.get()))

            #Tree view

            tree = ttk.Treeview(self)
            # Inserted at the root, program chooses id:
            tree.insert('', 'end', 'widgets', text='Widget Tour')
             
            # Same thing, but inserted as first child:
            tree.insert('', 0, 'gallery', text='Applications')

            # Treeview chooses the id:
            id = tree.insert('', 'end', text='Tutorial')

            # Inserted underneath an existing node:
            tree.insert('widgets', 'end', text='Canvas')
            tree.insert(id, 'end', text='Tree')
            tree.grid(row=1,sticky=tk.N+tk.E+tk.S+tk.W)



        pass

    def genGraph(self,path):
        if(path):
            pr.genGraph(pr.readData((fs.resource_path(path))),alpha=self.alpha.get(),weeks=self.weeks.get())
        else:
            tk.messagebox.showerror("Error","Por favor, cargue un archivo primero",parent=self)

    def doPronostic(self,path):
        if(path):
            data=pr.readData((fs.resource_path(path)))
            self.MAPE.set(pr.meanMAPE(data,alpha=self.alpha.get(),weeks=self.weeks.get()))
            self.ECM.set(pr.ECM(data,alpha=self.alpha.get(),weeks=self.weeks.get()))
            self.SD.set(pr.stdDeviation(data,alpha=self.alpha.get(),weeks=self.weeks.get()))
            self.CVD.set(pr.CVD(data,alpha=self.alpha.get(),weeks=self.weeks.get()))
        else:
            tk.messagebox.showerror("Error","Por favor, cargue un archivo primero",parent=self)

    def funcioncita(self, option):
        if(option=="Agregar producto..."):
            tk.messagebox.showinfo("CREAR PRODUCTO","CREANDO PRODUCTO")

    def getOptAlpha(self,path):
        if(path):
            alpha=pr.findOptimalAlpha(pr.readData((fs.resource_path(path))),alpha=self.alpha.get(), weeks=self.weeks.get())[0]
            self.alpha.set(alpha)
        else:
            tk.messagebox.showerror("Error","Por favor, cargue un archivo primero",parent=self)


    def openFile(self):
        filePath=tk.filedialog.askopenfilename(filetypes=(("Archivos CSV","*.csv"),),parent=self)
        if(filePath):
            self.filePath=filePath
            self.fileName.set("Nombre de archivo: "+fs.baseName(self.filePath))
        else:
            self.filePath=filePath
            self.fileName.set("Cargue un archivo porfavor")        




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
