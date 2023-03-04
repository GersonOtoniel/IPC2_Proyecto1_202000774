from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from ListaSimple import ListaSimple



class Menu:

    def Menu(self):
        while True:
            print("\n\n\n       ----------------------- Menu de opciones ------------------------")
            print()
            print(" 1. Abrir Muestra \n 2. Graficar \n 3. Salir")
            entrada = input("\nEscribir opción: ")

            if int(entrada) == 1:
                archivo = askopenfilename()
                archivoxml = minidom.parse(archivo)
                self.abrir(archivoxml)

            if int(entrada)==2:
                self.creargrafica() 

            if int(entrada)==3:
                system("cls")
                break       

            
    def abrir(self, archivo):

        filas = archivo.getElementsByTagName("filas")
        columnas = archivo.getElementsByTagName("columnas")
        codigo = archivo.getElementsByTagName("muestra")
        celdaviva = archivo.getElementsByTagName("celdaViva")
       

        self.fila = filas[0].childNodes[0].data
        self.columna = columnas[0].childNodes[0].data
        self.codigo = codigo[0].childNodes[0].data

        self.nuevo = ListaSimple()
        for i in range(len(celdaviva)):
            
            codigoviva = celdaviva[i].childNodes[5].firstChild.data
            xviva = celdaviva[i].childNodes[3].firstChild.data
            yviva = celdaviva[i].childNodes[1].firstChild.data
            self.nuevo.insertar(codigoviva, xviva, yviva)

        #self.nuevo.recorrerLista()
        


    def creargrafica(self):
        #filax = self.fila 
        graph = """ digraph grid
         {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        layout=dot 
        labelloc = "t"
        node [shape=record]
        

        edge [weight=1000 style=dashed color=dimgrey] 

        """  
        graph+=f''' label = "{self.codigo}" '''
        graph+=""" matriz [ label="{x,y"""
        
       
        
        for j in range(int(self.fila)):
            nodos = "|" + str(j)
            graph+=nodos
        graph+="}"
        

        """
        for k in range(int(self.columna)):
            graph+="|"
            graph+="{" + str(k)
            for l in range(int(self.fila)):
                nodosiguiente = "|"
                graph+=nodosiguiente
            graph+="}"
        graph+="}\""

        graph+="]"
        graph+="\n}"
        """
        for e in range(int(self.columna)):
            graph+="|"
            graph+="{" + str(e)
            for r in range(int(self.fila)):
                actual = self.nuevo.primero
                while actual != None:
                    if int(actual.x) == e and int(actual.y)== r:
                        graph+= actual.dato + "|"    
                    actual = actual.siguiente 
                graph+="|"
            if e != int(self.columna):    
                graph+="}"
                
        
        graph+="}\""            

        graph+="]"
        graph+="\n}"    
 
        archivo = open("src/ejemplograph.dot","w")
        archivo.write(graph)        

        #print(graph)




men = Menu()
men.Menu()