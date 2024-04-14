class Task:
    def __init__(self, name, status, user, proyecto):
        self.name = name
        self.status = status
        self.asignee = user
        self.proyecto = proyecto
        
    def __str__(self) -> str:
        return f'Tarea: {self.name}\nAsignada a: {self.asignee.name}\nEstado: {self.status}\nProyecto: {self.proyecto.nombre}'