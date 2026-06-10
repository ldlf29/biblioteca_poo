from abc import ABC, abstractmethod 
#importamos herramienta para hacer clases abstractas de la librería abc (Abstract Base Class)

class Material(ABC):
#Creamos la clase abstracta "Material" (padre) que va a ser heredara por las clases hijas (Libro y Revista)

    _next_id = 1

    def __init__(self, titulo, autor, año):
        self.id = Material._next_id
        Material._next_id += 1
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True

    @abstractmethod #Decorador
    def tipo(self): #Las subclases (hijas) lo definen.
        pass #indica que este metodo no hace nada por si solo, debe ser implementado por las clases hijas

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.id}] {self.tipo()} - '{self.titulo}' de {self.autor} ({self.año}) - {estado}"

#Herencias

class Libro(Material): #Hereda todo los atributos y metodos de la clase material.

    def __init__(self, titulo, autor, año, isbn, editorial):
        super().__init__(titulo, autor, año) #Super nos permite acceder a los atributos de la clase padre.
        #Atributos exclusivos de esta clase
        self.isbn = isbn 
        self.editorial = editorial

    def tipo(self): #Se cumple el contrato que exigia @abtractmethod de la clase padre (Material)
        return "Libro"

    def __str__(self):
        base = super().__str__() #Llama al metodo str de la clase padre para no repetir codigo
        return f"{base} | ISBN: {self.isbn}, Editorial: {self.editorial}"

class Revista(Material):

    def __init__(self, titulo, autor, año, numero, categoria):
        super().__init__(titulo, autor, año)
        self.numero = numero
        self.categoria = categoria

    def tipo(self):
        return "Revista"

    def __str__(self):
        base = super().__str__()
        return f"{base} | Numero: {self.numero}, Categoria: {self.categoria}"
