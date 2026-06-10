from datetime import date
#Importo herramienta nativa de Python para trabajar con el tiempo. Date maneja año, mes, dia.

class Prestamo:

    next_id = 1

    def __init__(self, socio, material):
        self.id = Prestamo.next_id
        Prestamo.next_id += 1
        self.socio = socio #Asociacion: referencia al socio que pidio el prestamo
        self.material = material #Asociacion: referencia al material prestado
        self.fecha_prestamo = date.today() #Fecha exacta del sistema al momento de crear el prestamo
        self.activo = True #True = prestamo vigente, False = ya fue devuelto
        self.fecha_devolucion = None #None hasta que se registre la devolucion

    def registrar_devolucion(self):
        #Marca el prestamo como devuelto y guarda la fecha
        self.activo = False
        self.fecha_devolucion = date.today()

    def __str__(self):
        estado = "ACTIVO" if self.activo else "DEVUELTO"
        texto = (f"[Prestamo {self.id}] {estado}\n"
                 f"  Material: {self.material.titulo} ({self.material.tipo()})\n"
                 f"  Socio: {self.socio.nombre_completo()}\n"
                 f"  Fecha prestamo: {self.fecha_prestamo}")
        if self.fecha_devolucion is not None: #Si ya se devolvio, mostrar la fecha
            texto += f"\n  Fecha devolucion: {self.fecha_devolucion}"
        return texto
