'''
Created on 02/08/2013

@author: Danny
'''
from graficador import Graficador
import ctypes

## \brief Clase que maneja las validaciones del numero dentro del tablero.
class Validador:

    def __init__(self,Sudoku):
        """Contructor
            Se Inicializa la variable del tablero para tener acceso a este y creamos un objeto de tipo graficador para poder pintar el tablero.
            Parametro:
            s El objeto padre de tipo Sudoku que crea a este objeto."""
        self.sudoku=Sudoku
        self.graficador=Graficador(self.sudoku)
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
        
    def Relacionar(self):
        """Pasa de la imagen de la ficha a un entero que corresponde al numero de la imagen."""
        self.sudoku.numeros=[]
        for i in range(9):
            n=[]
            for j in range(9):
                n.append(int(self.sudoku.cajas[i][j].accessibleName()))
            self.sudoku.numeros.append(n)
            
    def ValidarEspaciosVacios(self):
        """Verifica si el en tablero hay algun espacio vacio
            Retorna: 1 -> Completo , 0 -> Incompleto."""
        for i in range(9):
            for j in range(9):
                if self.sudoku.numeros[i][j]==0:
                    return 0
        return 1
    
    def SubCuadros(self):
        """Extrae la subcuadricula en la que se va a buscar algun posible numero repetido.
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos"""
        contador = 0
        self.sudoku.subnumeros=[]
        for i in range(3):
            self.sudoku.subnumeros.append([0]*3)
        #Primer SubCuadro
        for i in range(3):
            for j in  range(3):
                self.sudoku.subnumeros[i][j] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(0, 0)
        #Segundo SubCuadro
        for i in range(3):
            for j in  range(3,6):
                self.sudoku.subnumeros[i][j-3] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(0, 3)
        #Tercer SubCuadro
        for i in range(3):
            for j in  range(6,9):
                self.sudoku.subnumeros[i][j-6] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(0, 6)
        #Cuarto SubCuadro
        for i in range(3,6):
            for j in  range(3):
                self.sudoku.subnumeros[i-3][j] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(3, 0)
        #Quinto SubCuadro
        for i in range(3,6):
            for j in  range(3,6):
                self.sudoku.subnumeros[i-3][j-3] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(3, 3)
        #Sexto SubCuadro
        for i in range(3,6):
            for j in  range(6,9):
                self.sudoku.subnumeros[i-3][j-6] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(3, 6)
        #Septimo SubCuadro
        for i in range(6,9):
            for j in  range(3):
                self.sudoku.subnumeros[i-6][j] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(6, 0)
        #Octavo SubCuadro
        for i in range(6,9):
            for j in  range(3,6):
                self.sudoku.subnumeros[i-6][j-3] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(6, 3)
        #Noveno SubCuadro
        for i in range(6,9):
            for j in range(6,9):
                self.sudoku.subnumeros[i-6][j-6] = self.sudoku.numeros[i][j]
        contador = contador + self.VerificarSubCuadro()
        if not(self.VerificarSubCuadro()):
            self.graficador.pintaSub(6, 6)
        if contador == 9:
            return 1
        return 0
                   
    def VerificarSubCuadro(self):
        """Valida que no existan numeros repetidos en la subcuadricula.
            En caso de haber algun numero repetido en la subcuadricula, se pinta dicha subcuadricula.
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos"""
        for i in range(3):
            for j in range(3):
                numero = self.sudoku.subnumeros[i][j]
                if numero != 0:
                    for k in range(3):
                        for l in range(3):
                            if i != k or j != l:
                                if numero == self.sudoku.subnumeros[k][l]:
                                    return 0
        return 1
    
    def ValidarX(self):
        """Recorre el tablero linea a linea para encontrar numeros repetidos
        Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        b = 1
        for i in range(9):
            b = self.ValidaLinea(i)
            if b == 0:
                self.graficador.pintaX(i)
                return 0
        return 1
            
    def ValidaLinea(self,i):
        """Busca en la linea i si existe algun numero repetido.
            Parametro: i Linea donde se buscara.
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        fichas=[0]*10
        for j in range(9):
            indice = self.sudoku.numeros[i][j]
            fichas[indice] = fichas[indice] + 1
        return self.VerificaArregloIndices(fichas)
    
    def ValidarY(self):
        """Recorre el tablero columna a columna para encontrar numeros repetidos
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        b = 1
        for j in range(9):
            b = self.ValidaColumna(j)
            if b == 0:
                self.graficador.pintaY(j)
                return 0
        return 1
            
    def ValidaColumna(self,j):
        """Busca en la columna j si existe algun numero repetido.
            Parametro: j Columna donde se buscara.
            Retorna: Valor: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        fichas=[0]*10
        for i in range(9):
            indice = self.sudoku.numeros[i][j]
            fichas[indice] = fichas[indice] + 1
        return self.VerificaArregloIndices(fichas)
    
    def VerificaArregloIndices(self,fichas):
        """Verifica el numero de veces que se repite un numero.
            Si algun numero se repite mas de una vez, entonces existe algun repetido.
            Parametro: fichas Numero de ocurrencias de cada numero.
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        for i in range(1,10):
            if fichas[i] > 1:
                return 0
        return 1
    
    def Validaciones(self):
        """Maneja todas las validaciones y muestra un mensaje al usuario de acuerdo al tipo de error.
            Retorna: 1 -> Correcto , 0 -> Existen numeros repetidos."""
        b=1
        if not(self.sudoku.invalida):
            return 1
        if not(self.ValidarX()):
            self.MessageBox(None,"Existen Numeros Repetidos En Las Filas..!","ERROR",self.MB_ICONERROR)
            self.graficador.pintaTablero()
            b=0
        if not(self.ValidarY()):
            self.MessageBox(None,"Existen Numeros Repetidos En Las Columnas..!","ERROR",self.MB_ICONERROR)
            self.graficador.pintaTablero()
            b=0
        if not(self.SubCuadros()):
            self.MessageBox(None,"Existen Numeros Repetidos En Las Sub-Cuadriculas..!","ERROR",self.MB_ICONERROR)
            self.graficador.pintaTablero()
            b=0
        return b