import test
import filesSupport as fs
import machines as mc
import structure as st
import winsound
import pronostics as pr
import tkinter as tk
import math as m
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
            height, width, title = 500, 900, self.titleMod4

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
        master.resizable(False,False)
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
            for i in range(1,12):
                self.rowconfigure(i,weight=1)
            nameLabel.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S,columnspan=2,rowspan=2)

            #Show MPS

            showMPS = tk.Button(
            self, text="Mostrar Plan Maestro de Producción",
            command = lambda : self.showMPS(self.filePath))
            showMPS.grid(row=2,sticky=tk.W+tk.E+tk.S+tk.N,columnspan=2)


            loadData = tk.Button(
            self, text="Cargar datos históricos",
            command = lambda : self.openFile())
            loadData.grid(row=3,sticky=tk.W+tk.E+tk.S+tk.N)

            
            genPronostic = tk.Button(
            self, text="Graficar pronostico",
            command=lambda : self.genGraph(self.filePath))
            genPronostic.grid(row=3,column=1,sticky=tk.W+tk.E+tk.N+tk.S)

            doPronostic = tk.Button(
            self, text="Calcular Variables",
            command=lambda : self.doPronostic(self.filePath))
            doPronostic.grid(row=4,column=1,sticky=tk.W+tk.E+tk.N+tk.S)


            optAlpha = tk.Button(
            self, text="Obtener Alpha óptimo",
            command=lambda : self.getOptAlpha(self.filePath))
            optAlpha.grid(row=4,column=0,sticky=tk.W+tk.E+tk.N+tk.S)

            #Weeks entry
            tk.Label(self,text="Semanas de historico: ").grid(row=5, column=0)
            self.weeks = tk.IntVar(value=12)
            tk.Entry(self,textvariable=self.weeks).grid(row=5, column=1,sticky=tk.W+tk.E)


            #Initial inventory

            tk.Label(self,text="Inventario inicial: ").grid(row=6, column=0)
            self.inventory = tk.IntVar(value=100)
            tk.Entry(self,textvariable=self.inventory).grid(row=6, column=1,sticky=tk.W+tk.E)


            #MPS 

            tk.Label(self,text="Lote de producción: ").grid(row=7, column=0)
            self.MPS = tk.IntVar(value=1000)
            tk.Entry(self,textvariable=self.MPS).grid(row=7, column=1,sticky=tk.W+tk.E)

            #Alpha entry
            tk.Label(self,text="Valor de alpha: ").grid(row=8, column=0)
            self.alpha = tk.DoubleVar(value=0.5)
            tk.Entry(self,textvariable=self.alpha).grid(row=8, column=1,sticky=tk.W+tk.E)

            #MAPE
            tk.Label(self,text="MAPE: ").grid(row=9, column=0)
            self.MAPE = tk.DoubleVar()
            tk.Label(self,textvariable=self.MAPE).grid(row=9, column=1,sticky=tk.W+tk.E)

            #ECM

            tk.Label(self,text="ECM: ").grid(row=10, column=0)
            self.ECM = tk.DoubleVar()
            tk.Label(self,textvariable=self.ECM).grid(row=10, column=1,sticky=tk.W+tk.E)

            #SD

            tk.Label(self,text="Desviación estandar: ").grid(row=11, column=0)
            self.SD = tk.DoubleVar()
            tk.Label(self,textvariable=self.SD).grid(row=11, column=1,sticky=tk.W+tk.E)

            #CVD

            tk.Label(self,text="CVD: ").grid(row=12, column=0)
            self.CVD = tk.DoubleVar()
            tk.Label(self,textvariable=self.CVD).grid(row=12, column=1,sticky=tk.W+tk.E)
            

        elif(modNumber==3):

            self.materials=[]
            self.indexMaterialsItems = {}

            #Conf of expansion
            self.columnconfigure(0,weight=2)
            self.columnconfigure(1,weight=1)
            #self.rowconfigure(0,weight=1)
            #self.rowconfigure(1,weight=1)
            self.rowconfigure(2,weight=1)


            #Product layout

            confTreeGrid = {"sticky": tk.N+tk.E+tk.S+tk.W}
            confButtonGrid = {"sticky": tk.N+tk.S}

            #Add element

            def createMaterial(name,duration,available,required,parentIndexItem):
                material=st.material(name,duration,available,required)
                if(material not in self.materials): #if the material is not yet in the list we only add it
                    self.materials.append(material)
                    self.indexMaterialsItems[name]=len(self.materials)-1
                else: #If the material is already in the list we count how many materials of the same type are there and the counter is added to the index
                    self.materials.append(material) 
                    count = self.materials.count(material)
                    self.indexMaterialsItems[name+str(count+1)]=len(self.materials)-1
                parent=None
                if(parentIndexItem!=""): #If there is a parent we search it using the dictionary
                    parent=self.materials[self.indexMaterialsItems[parentIndexItem]]   
                updateMaterialsTree("create",material=material,parent=parent)


            def addMaterial():
                
                """
                Adds element to the list of products and machines
                """
                #Create modal dialog
                w = self.modalDialog("Agregar material")

                frame = tk.Frame(w)
                frame.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

                #Conf expansion

                frame.columnconfigure(0,weight=1)
                frame.columnconfigure(1,weight=1)
                confLabel = {"column":0,"sticky":tk.E+tk.W,"pady":10}
                confEntry = {"column":1,"sticky":tk.E+tk.W,"pady":10}

                name = tk.StringVar()
                tk.Label(frame,text="Nombre del material: ").grid(confLabel,row=0)
                tk.Entry(frame,textvariable=name).grid(confEntry,row=0)

                duration = tk.IntVar()
                tk.Label(frame,text="Duracion: ").grid(confLabel,row=1)
                tk.Entry(frame,textvariable=duration).grid(confEntry,row=1)

                available = tk.IntVar()
                tk.Label(frame,text="Inventario actual: ").grid(confLabel,row=2)
                tk.Entry(frame,textvariable=available).grid(confEntry,row=2)


                required = tk.IntVar()
                parent = tk.StringVar()
                requiredByParent = tk.IntVar()

                if (self.tree.get_children()):
                    tk.Label(frame,text="Requeridos por el padre: ").grid(confLabel,row=4)
                    tk.Entry(frame,textvariable=requiredByParent).grid(confEntry,row=4)

                    tk.Label(frame,text="Padre: ").grid(confLabel,row=5)
                    tk.Entry(frame,textvariable=parent).grid(confEntry,row=5)

                else:
                    tk.Label(frame,text="Requeridos: ").grid(confLabel,row=3)
                    tk.Entry(frame,textvariable=required).grid(confEntry,row=3)

                tk.Button(frame,text="Crear", command = lambda : createMaterial(name.get(), duration.get(), available.get(), required.get(),parent.get())).grid(confLabel,row=5)
                tk.Button(frame,text="Cancelar",command=w.winfo_toplevel().destroy).grid(confEntry,row=5)
                self.center(w,True)
                w.wait_window()

            def delMaterial(items,recursive=False):

                #print(name, recursive)
                if(not recursive):
                    #print(name,type(name))
                    if(items and type(items) is tuple):
                        #print(self.products, self.materials, "antes")
                        for i in items:
                            if(self.tree.exists(i)):
                                self.delElement(self.tree.get_children(i),True)
                                if(i in self.indexMaterialsItems.keys()):
                                    index = self.indexMaterialsItems[i]
                                    #print(i, "antes de morir")
                                    parent = self.materials[index].parent
                                    if(parent):
                                        parent.delChild(self.materials[index])
                                    self.materials.pop(index)
                                    for j in self.indexMaterialsItems.keys():
                                        if self.indexMaterialsItems[j]>index:
                                            self.indexMaterialsItems[j]=self.indexMaterialsItems[j]-1
                                    self.indexMaterialsItems.pop(i)
                                #print(self.products, self.materials, "despues")
                                #print(i, "itemId")
                                updateMaterialsTree("delete", material=st.material(i, 0))
                else:
                    if(items and type(items) is tuple):
                        for i in items:
                            self.delElement(self.tree.get_children(i),True)
                            if(i in self.indexMaterialsItems.keys()):
                                index = self.indexMaterialsItems[i]
                                #print(i, "antes de morir")
                                parent = self.materials[index].parent
                                if(parent):
                                        parent.delChild(self.materials[index])
                                self.materials.pop(index)
                                for j in self.indexMaterialsItems.keys():
                                    if self.indexMaterialsItems[j]>index:
                                        self.indexMaterialsItems[j]=self.indexMaterialsItems[j]-1
                                self.indexMaterialsItems.pop(i)



            addMaterialButton = tk.Button(
            self, text="Agregar material",command = addMaterial)
            addMaterialButton.grid(confTreeGrid,row=0,column=0)

            #Delete element
            delMaterialButton = tk.Button(
            self, text="Borrar material seleccionado",command=lambda : delMaterial(self.tree.selection()))
            delMaterialButton.grid(confTreeGrid,row=1,column=0)

            #Net requirements button
            netRButton = tk.Button(
            self, text="Mostrar Requerimientos Netos de Materiales",command= lambda: 5)
            netRButton.grid(confTreeGrid,row=0,column=1,rowspan=2)

            #Tree view


            def updateMaterialsTree(action,material=None,parent=None):
                parentIndex=""
                requiredByParent = 0
                if(action=="create"):
                    if(parent): #If there is a parent, the index is the parent name, the required by parent is obtained
                        parentIndex = parent.name
                        childIndex = material.parent.children.index(material)
                        requiredByParent = material.parent.childrenRequired[childIndex]
                    count = self.materials.count(material)
                    itemName = material.name
                    if(count > 1): #If there is more than one material with the same name on the three a counter is added to the item id
                        itemName = itemName + str(count)

                    self.tree.insert(parentIndex, "end", itemName,text=material.name, values=(material.duration,material.available,material.required,requiredByParent))
                elif(action=="delete"):
                    self.tree.delete(material.name)

            
            columns = ["Duracion","Disponibilidad Inicial","Requerimiento bruto", "Requeridos por el padre"]
            self.tree = ttk.Treeview(self,columns=columns)

            for i in columns:
                self.tree.column(i,width=50)
                self.tree.heading(i,text=i)
            self.tree.heading("#0",text="Nombre del material")
            

            self.tree.grid(confTreeGrid,row=2,column=0,columnspan=2)
            self.winfo_toplevel().geometry("")


            


        elif(modNumber==4):
            self.products = []
            self.machines = []
            self.indexProductsItems = {}
            self.indexMachinesItems = {}

            #Conf of expansion
            self.columnconfigure(0,weight=2)
            self.columnconfigure(1,weight=1)
            #self.rowconfigure(0,weight=1)
            #self.rowconfigure(1,weight=1)
            self.rowconfigure(2,weight=1)

            #Product layout

            confTreeGrid = {"sticky": tk.N+tk.E+tk.S+tk.W}
            confButtonGrid = {"sticky": tk.N+tk.S}

            #Add element   
            addElementButton = tk.Button(
            self, text="Agregar elemento",command=self.addElement)
            addElementButton.grid(confTreeGrid,row=0,column=0)

            #Delete element
            delElementButton = tk.Button(
            self, text="Borrar elemento seleccionado",command=lambda : self.delElement(self.tree.selection()))
            delElementButton.grid(confTreeGrid,row=1,column=0)

            #Optimal combination
            optCombButton = tk.Button(
            self, text="Encontrar Combinación Optima de Productos",command= lambda: showOptimalComb())
            optCombButton.grid(confTreeGrid,row=0,column=1,rowspan=2)

            #Bottle Neck
            # bottleNeckButton = tk.Button(
            # self, text="Encontrar Cuello de Botella",command=lambda : 5)
            # bottleNeckButton.grid(confTreeGrid,row=1,column=1)

            def showOptimalComb():
                if(len(self.products)>1):
                    w=self.modalDialog("Combinacion optima")
                    optimal = mc.optimalCombination(*self.products)
                    for i,p in enumerate(self.products):
                        tk.Label(w,text="Cantidad de producto "+p.name+": "+str(optimal[i]),padx=40).grid(row=i)
                    self.center(w,True)
                    w.wait_window()
                else:
                    tk.messagebox.showerror("Ingrese más productos", "Por favor ingrese al menos 2 productos para realizar el cálculo")


            #Tree view
            columns = ["Demanda","PPU","Duracion","Disponibilidad","Cantidad"]
            self.tree = ttk.Treeview(self,columns=columns)

            for i in columns:
                self.tree.column(i,width=50)
                self.tree.heading(i,text=i)
            self.tree.heading("#0",text="Nombre del producto/máquina")
            

            self.tree.grid(confTreeGrid,row=2,column=0,columnspan=2)
            self.winfo_toplevel().geometry("")


    def addElement(self):
        """
        Adds element to the list of products and machines
        """
        #Create modal dialog
        w = self.modalDialog("Agregar elemento")

        #Conf expansion

        w.columnconfigure(0,weight=1)
        w.columnconfigure(1,weight=1)

        tk.Label(w,text="Tipo de elemento:").grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.S+tk.W+tk.E,pady=10)

        kind = tk.StringVar(value="Producto")
        confLabel = {"column":0,"sticky":tk.E+tk.W,"pady":10}
        window=w
        w=tk.Frame(window)
        tk.Radiobutton(window,text="Producto",variable=kind,value="Producto", command=lambda: self.changeType(w,kind)).grid(confLabel,row=1,column=0)
        tk.Radiobutton(window,text="Maquina",variable=kind,value="Máquina",command=lambda: self.changeType(w,kind)).grid(confLabel,row=1,column=1)
        self.changeType(w, kind)
        
        w.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
        self.center(window,True)
        window.wait_window()

    def changeType(self,w,kind):
        """
        Accomodates the frame entries and labels
        """
        #print("Change of type!")
        for i in w.grid_slaves():
            i.destroy()
        confLabel = {"column":0,"sticky":tk.E+tk.W,"pady":10}
        confEntry = {"column":1,"sticky":tk.E+tk.W,"pady":10}

        name = tk.StringVar()
        tk.Label(w,text="Nombre del elemento: ").grid(confLabel,row=0)
        tk.Entry(w,textvariable=name).grid(confEntry,row=0)
        if(kind.get()=="Producto"):
            tk.Label(w,text="Demanda: ").grid(confLabel,row=1)
            tk.Label(w,text="Precio por unidad: ").grid(confLabel,row=2)

            
            #In case of a product
            demand = tk.IntVar()
            priceUnit = tk.IntVar()
            tk.Entry(w,textvariable=demand).grid(confEntry,row=1)
            tk.Entry(w,textvariable=priceUnit).grid(confEntry,row=2)

            tk.Button(w,text="Crear", command = lambda: self.createProduct(name.get(), demand.get(), priceUnit.get()) ).grid(confLabel,row=3)
            tk.Button(w,text="Cancelar",command=w.winfo_toplevel().destroy).grid(confEntry,row=3)

        elif(kind.get()=="Máquina"):
            tk.Label(w,text="Duracion: ").grid(confLabel,row=1)
            tk.Label(w,text="Disponibilidad: ").grid(confLabel,row=2)
            tk.Label(w,text="Cantidad: ").grid(confLabel,row=3)

            #In case of a machine
            duration = tk.IntVar()
            disponibility = tk.IntVar(value=2400)
            quantity = tk.IntVar(value=1)
            tk.Entry(w,textvariable=duration).grid(confEntry,row=1)
            tk.Entry(w,textvariable=disponibility).grid(confEntry,row=2)
            tk.Entry(w,textvariable=quantity).grid(confEntry,row=3)


            #Combo for the parent
            tk.Label(w,text="Padre: ").grid(confLabel,row=4)
            parentName = tk.StringVar()
            combo = ttk.Combobox(w,textvariable=parentName,state='readonly',width=30,justify=tk.CENTER)
            if(self.products):
                values=[i.name for i in self.products]
                for i,v in enumerate(values):
                    self.indexProductsItems[v]=i
                if(self.machines):
                    for i,v in enumerate(self.machines):
                        value=v.name
                        if(v.name in values):
                            value=value+str(values.count(v.name)+1)
                        values.append(value)
                        self.indexMachinesItems[value]=i
                combo['values']=values
            else:
                combo['values']=["Agrega primero un producto"]
            combo.grid(confEntry,row=4)
            # combo.bind('<<ComboboxSelected>>', lambda x : self.funcioncita(combo.get()))

            def createMachine():
                self.createMachine(name.get(), duration.get(), disponibility.get(), quantity.get(),parentName.get())
                updateCombo()
                #print(self.indexMachinesItems, "despues de crear")

            def updateCombo():
                if(self.products):
                    values=[i.name for i in self.products]
                    for i,v in enumerate(values):
                        self.indexProductsItems[v]=i
                    if(self.machines):
                        for i,v in enumerate(self.machines):
                            value=v.name
                            if(v.name in values):
                                value=value+str(values.count(v.name)+1)
                            values.append(value)
                            self.indexMachinesItems[value]=i
                    combo['values']=values
                else:
                    combo['values']=["Agrega primero un producto"]


            tk.Button(w,text="Crear",command = createMachine).grid(confLabel,row=5)
            tk.Button(w,text="Cancelar",command=w.winfo_toplevel().destroy).grid(confEntry,row=5)

        #Adjust window to the new contents
        w.winfo_toplevel().geometry("")

        


    def modalDialog(self,title):
        w = tk.Toplevel(self)
        w.transient(self)
        w.grab_set()
        #w.resizable(False,False)
        w.wm_title(title)
        w.iconbitmap(self.iconPath)
        return w

    def createProduct(self,name,demand,priceUnit):
        product=mc.product(name, demand, priceUnit)
        if(product not in self.products):
            self.products.append(product)
            self.indexProductsItems[name]=len(self.products)-1
            self.updateProductTree("create","product",machine=product)
        else:
            tk.messagebox.showerror("Elemento ya existente","El producto "+name+" ya existe")

    def delElement(self,name,recursive=False):
        #print(name, recursive)
        if(not recursive):
            #print(name,type(name))
            if(name and type(name) is tuple):
                #print(self.products, self.machines, "antes")
                for i in name:
                    if(self.tree.exists(i)):
                        self.delElement(self.tree.get_children(i),True)
                        if(i in self.indexMachinesItems.keys()):
                            index = self.indexMachinesItems[i]
                            #print(i, "antes de morir")
                            self.machines.pop(index)
                            for j in self.indexMachinesItems.keys():
                                if self.indexMachinesItems[j]>index:
                                    self.indexMachinesItems[j]=self.indexMachinesItems[j]-1
                            self.indexMachinesItems.pop(i)
                        elif(i in self.indexProductsItems.keys()):
                            index = self.indexProductsItems[i]
                            self.products.pop(index)
                            for j in self.indexProductsItems.keys():
                                if self.indexProductsItems[j]>index:
                                    self.indexProductsItems[j]=self.indexProductsItems[j]-1
                            self.indexProductsItems.pop(i)
                        #print(self.products, self.machines, "despues")
                        #print(i, "itemId")
                        self.updateProductTree("delete", "product", machine=mc.product(i, 0, 0))
        else:
            if(name and type(name) is tuple):
                for i in name:
                    self.delElement(self.tree.get_children(i),True)
                    if(i in self.indexMachinesItems.keys()):
                        index = self.indexMachinesItems[i]
                        #print(i, "antes de morir")
                        self.machines.pop(index)
                        for j in self.indexMachinesItems.keys():
                            if self.indexMachinesItems[j]>index:
                                self.indexMachinesItems[j]=self.indexMachinesItems[j]-1
                        self.indexMachinesItems.pop(i)
                    elif(i in self.indexProductsItems.keys()):
                        index = self.indexProductsItems[i]
                        self.products.pop(index)
                        for j in self.indexProductsItems.keys():
                            if self.indexProductsItems[j]>index:
                                self.indexProductsItems[j]=self.indexProductsItems[j]-1
                        self.indexProductsItems.pop(i)




    def createMachine(self,name,duration,disponibility,quantity,parentIndexItem):
        machine=mc.machine(name, duration, disponibility,quantity)
        self.machines.append(machine)
        if(parentIndexItem in self.indexProductsItems.keys()):
            parent=self.products[self.indexProductsItems[parentIndexItem]]
        elif(parentIndexItem in self.indexMachinesItems.keys()):
            parent=self.machines[self.indexMachinesItems[parentIndexItem]]
        self.updateProductTree("create","machine",parentIndexItem,machine)
        parent.addChildren(machine)
        


    def updateProductTree(self,action,kind,parentId="",machine=None):
        """
        Updates the tree based on the products and machines lists
        """
        
        if(action=="create"):
            #print("inserting")
            if(kind=="product"):
                self.tree.insert("", "end", machine.name,text=machine.name, values=(machine.demand,machine.priceUnit))
            if(kind=="machine"):
                count = self.machines.count(machine)
                #print(count,"count")
                if(count>1):
                    #print(self.tree.get_children(), "items arbol")
                    #print(machine.name+str(count), "id")
                   # print(parentId, "parentId")
                    self.tree.insert(parentId,"end", machine.name+str(count),text=machine.name, values=("", "", machine.duration, machine.disponibility, machine.quantity))
                else:
                    self.tree.insert(parentId,"end", machine.name,text=machine.name, values=("", "", machine.duration, machine.disponibility, machine.quantity))
        elif(action=="delete"):
                #print("deleting")
                self.tree.delete(machine.name)
        #print(self.indexMachinesItems,self.indexProductsItems,"despues de cualquier modificacion")

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

    def showMPS(self,path):
        if(path):
            conf = {"borderwidth": 1 , "relief": tk.SOLID, "padx": 10, "pady": 5}
            #Create modal dialog
            w = self.modalDialog("Plan Maestro de Produccion")
            #Data
            data=pr.readData((fs.resource_path(path)))

            weeksRemaining=len(data)-self.weeks.get()

            #Create title
            tk.Label(w,text="Semanas",cnf=conf).grid(row=0, column=1, columnspan=weeksRemaining+1, sticky=tk.W+tk.E+tk.N+tk.S)
            
            tk.Label(w,text="Plan Maestro de Producción",cnf=conf).grid(row=0,column=0, rowspan=2,sticky=tk.W+tk.E+tk.N+tk.S)
            
            #Enumerate weeks
            for i in range(weeksRemaining):
                w.columnconfigure(1+i,weight=2)
                tk.Label(w,text=str(i+1+self.weeks.get()), cnf=conf).grid(row=1,column=1+i,sticky=tk.W+tk.E+tk.N+tk.S)

            #First Column
            tk.Label(w,text="Pronóstico", cnf=conf).grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
            tk.Label(w,text="Ordenes", cnf=conf).grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
            tk.Label(w,text="Inventario", cnf=conf).grid(row=4, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
            tk.Label(w,text="MPS", cnf=conf).grid(row=5, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
            tk.Label(w,text="DPP", cnf=conf).grid(row=6, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

            #Row adjust
            for i in range(7):
                w.rowconfigure(i,weight=1)


            #New config
            conf = {"padx": 20, "pady": 10}

            #Pronostic and orders
            pronostic = pr.calcPronostic(data,weeks=self.weeks.get(),alpha=self.alpha.get())
            #Get inventories and stuff
            inventories, MPS, DPP = pr.getInventory(data, self.MPS.get(), initial=self.inventory.get(), pronostic=pronostic, weeks=self.weeks.get(), alpha=self.alpha.get())
            for i in range(len(pronostic)-1):
                tk.Label(w,text=str(m.floor(pronostic[i])),cnf=conf).grid(row=2,column=i+1,sticky=tk.W+tk.E+tk.N+tk.S)
                tk.Label(w,text=str(int(data[i+self.weeks.get()])),cnf=conf).grid(row=3,column=i+1,sticky=tk.W+tk.E+tk.N+tk.S)
                tk.Label(w,text=str(inventories[i]), cnf=conf).grid(row=4,column=i+1,sticky=tk.W+tk.E+tk.N+tk.S)
                tk.Label(w,text=str(MPS[i]), cnf=conf).grid(row=5,column=i+1,sticky=tk.W+tk.E+tk.N+tk.S)
                tk.Label(w,text=str(DPP[i]), cnf=conf).grid(row=6,column=i+1,sticky=tk.W+tk.E+tk.N+tk.S)

            self.center(w,True)
            w.wait_window()
        else:
            tk.messagebox.showerror("Error","Por favor, cargue un archivo primero",parent=self)



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
