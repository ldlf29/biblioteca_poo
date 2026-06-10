# Gestión de errores. Heredamos de la clase Exception de Python para que nuestras clases actúen como errores.

class MaterialNoDisponible(Exception): # Clase para cuando un material ya está prestado e intentan pedirlo de nuevo.
    def __init__(self, material_id): # Método constructor. Recibe el ID del material que falló.
        super().__init__(f"El material con ID {material_id} no está disponible") # Llama al constructor de la clase padre (Exception) y define el mensaje de error.
        self.material_id = material_id # Guarda el ID del material para poder saber cuál falló.

class SocioNoEncontrado(Exception): # Clase para cuando buscamos un socio por ID y no existe en la biblioteca.
    def __init__(self, socio_id): # Recibe el ID del socio que no se encontró.
        super().__init__(f"No se encontró el socio con ID {socio_id}") # Llama al constructor de Exception con el mensaje correspondiente.
        self.socio_id = socio_id # Guarda el ID del socio que no se encontró.

class MaterialNoEncontrado(Exception): # Clase para cuando buscamos un material por ID y no existe en la biblioteca.
    def __init__(self, material_id): # Recibe el ID del material que no existe.
        super().__init__(f"No se encontró el material con ID {material_id}") # Llama al constructor de Exception con el mensaje de error.
        self.material_id = material_id # Guarda el ID del material que no se encontró.

class PrestamoNoEncontrado(Exception): # Clase para cuando buscamos un préstamo por ID y no existe en la biblioteca.
    def __init__(self, prestamo_id): # Recibe el ID del préstamo que no existe.
        super().__init__(f"No se encontró el préstamo con ID {prestamo_id}") # Llama al constructor de Exception con el mensaje de error.
        self.prestamo_id = prestamo_id # Guarda el ID del préstamo que no se encontró.