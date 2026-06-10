class Socio:

    next_id = 1 #Variable para que cada usuario tenga un id unico

    def __init__(self, nombre, apellido, dni): 
    #Metodo constructor. Self representa al objeto que se esta creando en ese instante. Atributos de instancia.
        self.id = Socio.next_id #se asigna el id unico al objeto
        Socio.next_id += 1 #se incrementa el id para el siguiente objeto
        self.nombre = nombre #se asigna el nombre al objeto
        self.apellido = apellido #se asigna el apellido al objeto
        self.dni = dni #se asigna el dni al objeto

    def nombre_completo(self): #Retorna el nombre y apellido juntos.
        return f"{self.nombre} {self.apellido}" #f es para formatear string y poder inyectar variables dentro del texto.
        #Este metodo se hizo por si en un futuro quisiera agregar segundo nombre, apodo

    def __str__(self): #__str__ indica como debe comportarse el objeto
        return f"[{self.id}] {self.nombre_completo()} - DNI: {self.dni}" #Construye el texto final a mostrar
