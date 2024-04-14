class Proyecto:
    def __init__(self, nombre, descripcion, equipo, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.equipo = equipo
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return f"Proyecto: {self.nombre}\n Descripcion: {self.descripcion}\n Equipo: {self.equipo.id}\nFecha Inicio: {self.fecha_inicio}\n" 