from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from ListaSimple import ListaSimple
from ListaOrganismo import ListaOrganismo



class Menu:

    def Menu(self):
        while True:
            print("\n\n\n       ----------------------- Menu de opciones ------------------------")
            print()
            print(" 1. Abrir Muestra \n 2. Graficar con datos iniciales \n 3. Insertar célula \n 4. Salir")
            entrada = input("\nEscribir opción: ")

            if int(entrada) == 1:
                archivo = askopenfilename()
                archivoxml = minidom.parse(archivo)
                self.abrir(archivoxml)

            if int(entrada)==2:
                self.creargrafica()
                 

            if int(entrada)==3:
                system("cls")
                self.insertarcelula()
            
            if int(entrada)==4:
                system("cls")
                break
            if int(entrada)==5:
                self.jugadavalida()

            
    def abrir(self, archivo):

        filas = archivo.getElementsByTagName("filas")
        columnas = archivo.getElementsByTagName("columnas")
        codigo = archivo.getElementsByTagName("muestra")
        celdaviva = archivo.getElementsByTagName("celdaViva")
        organismos = archivo.getElementsByTagName("organismo")
        

        self.fila = filas[0].childNodes[0].data
        self.columna = columnas[0].childNodes[0].data
        self.codigo = codigo[0].childNodes[0].data

        #Aquí se agrega la fila y la columna de cada celula como coordenadas x-y al igual que su codigo
        self.nuevo = ListaSimple()
        for i in range(len(celdaviva)):
            codigoviva = celdaviva[i].childNodes[5].firstChild.data
            xviva = celdaviva[i].childNodes[3].firstChild.data
            yviva = celdaviva[i].childNodes[1].firstChild.data
            self.nuevo.insertar(codigoviva, xviva, yviva)
        self.nuevo.recorrerLista()

        #Aquí se agrega el nombre y el codigo de los organismos en una lista simple
        letra = 65
        self.organismo = ListaOrganismo()
        for j in range(len(organismos)):
            codigo = organismos[j].childNodes[1].firstChild.data
            nombre = organismos[j].childNodes[3].firstChild.data
            self.organismo.insertar(nombre, codigo, chr(letra))
            letra+=1

        self.organismo.recorrerLista()    
        

    def creargrafica(self):
        #filax = self.fila 
        self.graph = """ digraph grid {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        layout=dot 
        labelloc = "t"
        node [shape=record]

        edge [weight=1000 style=dashed color=dimgrey] 

        """  
        self.graph+=f''' label = "{self.codigo}" '''
        self.graph+=""" matriz [ label="{x,y"""
       
        
        for j in range(int(self.fila)):
            nodos = "|" + str(j)
            self.graph+=nodos
        self.graph+="}"
        
        #Aquí se crean las columnas y filas. Si las coordenadas coinciden con las de las ingresadas por cada celula si insertara en ese lugar la celula
        for e in range(int(self.columna)):
            self.graph+="|"
            self.graph+="{" + str(e)
            count = 0
            for r in range(int(self.fila)):
                actual = self.nuevo.primero
                letter = None
                while actual != None:
                    if int(actual.x) == e and int(actual.y)== r:
                        actual2 = self.organismo.primero
                        while actual2 != None:
                            if actual.dato == actual2.codigo:
                                letter = actual2.letra
                                self.graph+= "|" + letter
                                count+=1   
                            actual2 = actual2.siguiente
                            
                    actual = actual.siguiente
                if count > 0:
                    self.graph+=""
                if count == 0:
                    self.graph+="|"
                count=0    
                   
            if e != int(self.columna):    
                self.graph+="}"
                
        
        self.graph+="\""            
        self.graph+="]"
        self.graph+="\n}"
         

        archivo = open('./src/ejemplograph.dot','w')
        archivo.write(self.graph)

       # system('dot -Tpdf ./src/ejemplograph.dot -o ./src/grafica.pdf')
        system('dot -Tpdf ./src/ejemplograph.dot -o ./src/ejemplograph.pdf')
        #system('cd ./grafica.png')


    def insertarcelula(self):

        count =0

        while True:
            if count == 0:
                self.fila = input("Inserte numero de fila: ")
                count+=1
            if count == 1:
                self.columna = input("Inserte numero de columna: ")
                count+=1
            if count == 2:
                self.codigo2 = input("Ingrese codigo del organismo: ")
                count+=1
            self.nuevo.insertar(self.codigo2, self.columna, self.fila)
            if count==3:
                self.nuevo.recorrerLista()
                count+=1
            if count == 4:
                entrada = input("Ingrese 5 para salir: ")
            if int(entrada) == 5:
                system("cls")
                break

            

    """
    def graficafinal(self):  
        for i in range(int(self.fila)):
            for j in range(int(self.columna)):
                actual = self.nuevo.primero
                while actual != None:
                    if i == int(actual.y) and j== int(actual.x):
                        print(actual.dato)
                    actual = actual.siguiente
    """   

    """
    def posicionvalida(self):
        
        count = 0
        count2 = 0
        count3 = 0
        for i in range(int(self.fila)):
            for j in range(int(self.columna)):
                actual = self.nuevo.primero
                while actual != None:
                    nodoactual = actual
                    if int(actual.y)==i and int(actual.x)== j:
                        if actual.dato == "SCP096":
                            count+=1
                        if actual.dato != "SCP096":
                            count2+=1
                        if count == 2:
                            while actual != None:
                                if actual.dato == "SCP096":
                                    count3+=1
                            
                                if count3 == 2:
                                    break
                                if actual.dato != "SCP096":
                                    actual.dato = "SCP096"
                                actual = actual.anterior    
                            actual = nodoactual     

                    actual = actual.siguiente
                
                            
        self.nuevo.recorrerLista()
        """



    def jugadavalida(self):
        self.px = int(self.columna)
        self.py = int(self.fila)
            
        
        
        self.px +1
        actual = self.nuevo.primero
        while actual != None:
            guardarnodo = actual
            if int(actual.x) == self.px and int(actual.y) == self.py:
                if actual.dato != self.codigo2:
                    continue
                self.px+=1
                if self.nuevo.indexsiguiente(self.px) != self.codigo2:
                    self.px+=1
                    if self.nuevo.indexsiguiente(self.px) == self.codigo2:
                        actual = actual.siguiente
                    actual.dato = self.codigo2
            actual = guardarnodo
            actual = actual.siguiente
                
                        
                  



               

men = Menu()
men.Menu()