from tkinter import Tk, Label, Button, Entry, Frame

class mi_ventana(Frame): #Clase

    def __init__(self,master=None): #Se llama el create_widgets desde el constructor
        super().__init__(master,width=320, height=300)
        self.master = master
        self.pack()
        self.create_widgets()

    def suma(self):             #se hace las 
        Mp = self.txt1.get()
        Mo = self.txt2.get()
        Pm = self.txt3.get()
        Gi = self.txt4.get()
        Go = self.txt5.get()
        Uti = self.txt6.get()
        
        Mate = float(Mp) / float(Pm)
        Ot = float(Gi) / float(Pm)
        G = float(Go) / float(Pm)
        O = float(Mo) / float(Pm)

        M = float(Uti)/100
        Costo_total = float(Mate) + float(Ot) + float(G) + float(O)

        PVe = float(Costo_total)/(1-float(M))

        self.txt7.delete(0, 'end')
        self.txt7.insert(0,PVe)

    def create_widgets(self):

        self.Lbl1 = Label(self, text="Materia prima total")
        self.Lbl1.place(x=10, y=10, width=100, height=30) 

        self.txt1 = Entry(self, bg="white")
        self.txt1.place(x=120, y=10, width=100, height=30) 

        self.Lbl2 = Label(self, text="Mano de Obra")
        self.Lbl2.place(x=10, y=50, width=100, height=30) 

        self.txt2 = Entry(self, bg="white")
        self.txt2.place(x=120, y=50, width=100, height=30) 

        self.Lbl3 = Label(self, text="Producto mensual")
        self.Lbl3.place(x=10, y=90, width=100, height=30) 

        self.txt3 = Entry(self, bg="white")
        self.txt3.place(x=120, y=90, width=100, height=30) 

        self.Lbl4 = Label(self, text="Gastos Indirectos",)
        self.Lbl4.place(x=10, y=130, width=100, height=30) 

        self.txt4 = Entry(self, bg="white")
        self.txt4.place(x=120, y=130, width=100, height=30) 

        self.Lbl5 = Label(self, text="Gastos Operativos")
        self.Lbl5.place(x=10, y=170, width=100, height=30) 

        self.txt5 = Entry(self, bg="white")
        self.txt5.place(x=120, y=170, width=100, height=30) 

        self.Lbl6 = Label(self, text="Utilidad")
        self.Lbl6.place(x=10, y=210, width=100, height=30) 

        self.txt6 = Entry(self, bg="white")
        self.txt6.place(x=120, y=210, width=100, height=30) 

        #Boton
        
        self.boton1 = Button(self, text="Calcular", command= self.suma) #se llama la clase suma desde self
        self.boton1.place(x=230, y=260, width=80, height=30)

        # Resultado final
        
        self.Lbl7 = Label(self, text="Precio de venta", bg="white")
        self.Lbl7.place(x=10, y=260, width=100, height=30) 

        self.txt7 = Entry(self, bg="white")
        self.txt7.place(x=120, y=260, width=100, height=30) 


root = Tk()
root.wm_title("Precio de venta")
app = mi_ventana(root)
app.mainloop()