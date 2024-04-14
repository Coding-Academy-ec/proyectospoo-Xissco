from equipos.equipo import Team, User
from proyectos.proyecto import Proyecto
from tareas.tarea import Task

def main():
    print("Gestión de Proyectos")
    print("Creación de Usuarios:")
    fguillen = User("Francisco Guillén", "fguillen@isteps.edu.ec")
    jdurazno = User("Jennifer Durazno", "jdurazno@isteps.edu.ec")
    print(str(jdurazno) + "\n" + str(fguillen) + "\n")
    
    print("Asignación del equipo:")
    equipo = Team(1)
    equipo.add_user(jdurazno)
    equipo.add_user(fguillen)
    print(str(equipo))
    
    print("Creación Proyecto")
    proyecto = Proyecto("Pagina Web Institucional", "Pagina Web del Instituto", equipo, "14/04/2024")
    print(str(proyecto) + "\n")
    
    print("Asignación de Tareas")
    task1 = Task("Marquetar Pagina Web", "En Curso", jdurazno, proyecto)
    task2 = Task("Programar Página", "En espera", fguillen, proyecto)
    print(str(task1) + "\n\n" + str(task2))

if __name__ == "__main__":
    main()
