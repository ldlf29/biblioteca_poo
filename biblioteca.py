from prestamo import Prestamo
from excepciones import (MaterialNoDisponible, SocioNoEncontrado, MaterialNoEncontrado, PrestamoNoEncontrado)

class Biblioteca: 
#Clase principal para la gestión del sistema de biblioteca. (Objeto principal contiene y administra otros objetos)

    def __init__(self, nombre): #Recibe como parametro el nombre de la biblioteca.
        self.nombre = nombre #Se le asigna el nombre a la biblioteca.
        self.materiales = [] #Se crea una lista para guardar los materiales.
        self.socios = [] #Se crea una lista para guardar los socios.
        self.prestamos = [] #Se crea una lista para guardar los prestamos.

#Gestion de materiales

    def agregar_material(self, material): #Recibe como parametro un material.
        self.materiales.append(material) #Se agrega el material al final de la lista.

    def buscar_material_por_id(self, material_id): #Recibe como parametro el ID de un material.
        i = 0 #Inicializa el contador.
        while i < len(self.materiales): #Recorre la lista de materiales.
            if self.materiales[i].id == material_id: #Si encuentra el material con el ID indicado.
                return self.materiales[i] #Lo devuelve.
            i += 1 #Sino, sigue buscando.
        raise MaterialNoEncontrado(material_id) #Si no encuentra el material, lanza una excepcion.

    def buscar_material_por_titulo(self, texto): #Recibe como parametro un texto.
        texto = texto.lower() #Convierte el texto a minusculas.
        resultados = [] #Crea una lista para guardar los resultados.
        i = 0
        while i < len(self.materiales):
            if texto in self.materiales[i].titulo.lower():
                resultados.append(self.materiales[i])
            i += 1
        return resultados

    def listar_materiales_disponibles(self): #Retorna una lista con los materiales disponibles.
        disponibles = [] #Crea una lista para guardar los materiales disponibles.
        i = 0
        while i < len(self.materiales):
            if self.materiales[i].disponible:
                disponibles.append(self.materiales[i])
            i += 1
        return disponibles

#Gestion de socios

    def agregar_socio(self, socio): #Recibe como parametro un socio.
        self.socios.append(socio) #Se agrega el socio a la lista.

    def buscar_socio_por_id(self, socio_id): #Recibe como parametro el ID de un socio.
        i = 0 #Inicializa el contador.
        while i < len(self.socios): #Recorre la lista de socios.
            if self.socios[i].id == socio_id: #Si encuentra el socio con el ID indicado.
                return self.socios[i] #Lo devuelve.
            i += 1 #Sino, sigue buscando.
        raise SocioNoEncontrado(socio_id) #Si no encuentra el socio, lanza una excepcion.

#Gestion de prestamos

    def registrar_prestamo(self, socio_id, material_id):
        socio = self.buscar_socio_por_id(socio_id)
        material = self.buscar_material_por_id(material_id)

        if not material.disponible: #Si el material no esta disponible.
            raise MaterialNoDisponible(material_id) #Lanza una excepcion.

        material.disponible = False #Marca el material como no disponible.
        prestamo = Prestamo(socio, material) #Crea un prestamo.
        self.prestamos.append(prestamo) #Lo agrega a la lista de prestamos.
        return prestamo

    def registrar_devolucion(self, prestamo_id):

        i = 0
        while i < len(self.prestamos):
            if self.prestamos[i].id == prestamo_id and self.prestamos[i].activo:
                self.prestamos[i].registrar_devolucion()
                self.prestamos[i].material.disponible = True
                return self.prestamos[i]
            i += 1
        raise PrestamoNoEncontrado(prestamo_id)

    def listar_prestamos_activos(self):
        activos = []
        i = 0
        while i < len(self.prestamos):
            if self.prestamos[i].activo:
                activos.append(self.prestamos[i])
            i += 1
        return activos
