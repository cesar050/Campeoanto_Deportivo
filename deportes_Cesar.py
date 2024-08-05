from datetime import datetime, time
from tabulate import tabulate

class Persona:
    def __init__(self, nombre, id, sexo, fecha_nacimiento):
        self._nombre = nombre
        self._id = id
        self._sexo = sexo
        self._fecha_nacimiento = fecha_nacimiento

class Jugador(Persona):
    def __init__(self, nombre, id, sexo, fecha_nacimiento, equipo):
        super().__init__(nombre, id, sexo, fecha_nacimiento)
        self._equipo = equipo
        self.id_jugador = id
        self.anotaciones = 0
        self.tarjeta_amarilla = 0
        self.tarjeta_roja = 0
        self.asistencias = 0

class Equipo:
    def __init__(self, id_equipo, nombre_equipo, costo_registro):
        self.id_equipo = id_equipo
        self.nombre_equipo = nombre_equipo
        self.costo_registro = costo_registro
        self.jugadores = []
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Campeonato:
    def __init__(self, nombre, premio):
        self.nombre = nombre
        self.premio = premio
        self.equipos = []
        self.jornadas = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def crear_jornadas(self):
        for i, equipo_local in enumerate(self.equipos):
            for j, equipo_visita in enumerate(self.equipos):
                if i != j:
                    jornada = Jornada(equipo_local, equipo_visita)
                    self.jornadas.append(jornada)

    def mostrar_tabla_posiciones(self):
        tabla = []
        for equipo in self.equipos:
            tabla.append([equipo.nombre_equipo, equipo.puntos, equipo.goles_a_favor, equipo.goles_en_contra])
        print(tabulate(tabla, headers=["Equipo", "Puntos", "Goles a Favor", "Goles en Contra"], tablefmt="grid"))

    def mostrar_estadisticas_jugadores(self):
        tabla = []
        for equipo in self.equipos:
            for jugador in equipo.jugadores:
                tabla.append([jugador._nombre, equipo.nombre_equipo, jugador.anotaciones, jugador.asistencias, jugador.tarjeta_amarilla, jugador.tarjeta_roja])
        print(tabulate(tabla, headers=["Jugador", "Equipo", "Goles", "Asistencias", "Tarjetas Amarillas", "Tarjetas Rojas"], tablefmt="grid"))

    def obtener_equipo_campeon(self):
        equipo_campeon = max(self.equipos, key=lambda equipo: equipo.puntos)
        return equipo_campeon.nombre_equipo

class Jornada:
    def __init__(self, equipo_local, equipo_visita):
        self.equipo_local = equipo_local
        self.equipo_visita = equipo_visita
        self.inicio_partido = None
        self.fin_partido = None

def ingresar_datos_campeonato():
    nombre = input("Ingrese el nombre del campeonato: ")
    premio = input("Ingrese el premio del campeonato: ")
    return Campeonato(nombre, premio)

def ingresar_equipos_y_jugadores(campeonato):
    num_equipos = int(input("Ingrese el número de equipos: "))
    for i in range(num_equipos):
        nombre_equipo = input(f"Ingrese el nombre del equipo {i + 1}: ")
        costo_registro = int(input(f"Ingrese el costo de registro del equipo {nombre_equipo}: "))
        equipo = Equipo(i + 1, nombre_equipo, costo_registro)
        num_jugadores = int(input(f"Ingrese el número de jugadores del equipo {nombre_equipo}: "))
        for j in range(num_jugadores):
            nombre_jugador = input(f"Ingrese el nombre del jugador {j + 1} del equipo {nombre_equipo}: ")
            id_jugador = input(f"Ingrese el ID del jugador {nombre_jugador}: ")
            sexo_jugador = input(f"Ingrese el sexo del jugador {nombre_jugador}: ")
            fecha_nacimiento_jugador = input(f"Ingrese la fecha de nacimiento del jugador {nombre_jugador} (YYYY-MM-DD): ")
            fecha_nacimiento_jugador = datetime.strptime(fecha_nacimiento_jugador, "%Y-%m-%d").date()
            jugador = Jugador(nombre_jugador, id_jugador, sexo_jugador, fecha_nacimiento_jugador, nombre_equipo)
            equipo.agregar_jugador(jugador)
        campeonato.agregar_equipo(equipo)

def ingresar_resultados_juegos(campeonato):
    for jornada in campeonato.jornadas:
        print(f"\nJornada: {jornada.equipo_local.nombre_equipo} vs {jornada.equipo_visita.nombre_equipo}")
        inicio_partido = input("Ingrese la hora de inicio del partido (HH:MM): ")
        fin_partido = input("Ingrese la hora de fin del partido (HH:MM): ")
        jornada.inicio_partido = datetime.strptime(inicio_partido, "%H:%M").time()
        jornada.fin_partido = datetime.strptime(fin_partido, "%H:%M").time()

        goles_local = int(input(f"Ingrese los goles del equipo {jornada.equipo_local.nombre_equipo}: "))
        goles_visita = int(input(f"Ingrese los goles del equipo {jornada.equipo_visita.nombre_equipo}: "))

        jornada.equipo_local.goles_a_favor += goles_local
        jornada.equipo_local.goles_en_contra += goles_visita
        jornada.equipo_visita.goles_a_favor += goles_visita
        jornada.equipo_visita.goles_en_contra += goles_local

        if goles_local > goles_visita:
            jornada.equipo_local.puntos += 3
        elif goles_local < goles_visita:
            jornada.equipo_visita.puntos += 3
        else:
            jornada.equipo_local.puntos += 1
            jornada.equipo_visita.puntos += 1

        for equipo in [jornada.equipo_local, jornada.equipo_visita]:
            for jugador in equipo.jugadores:
                goles = int(input(f"Ingrese los goles del jugador {jugador._nombre} del equipo {equipo.nombre_equipo}: "))
                asistencias = int(input(f"Ingrese las asistencias del jugador {jugador._nombre} del equipo {equipo.nombre_equipo}: "))
                amarillas = int(input(f"Ingrese las tarjetas amarillas del jugador {jugador._nombre} del equipo {equipo.nombre_equipo}: "))
                rojas = int(input(f"Ingrese las tarjetas rojas del jugador {jugador._nombre} del equipo {equipo.nombre_equipo}: "))
                jugador.anotaciones += goles
                jugador.asistencias += asistencias
                jugador.tarjeta_amarilla += amarillas
                jugador.tarjeta_roja += rojas

def main():
    campeonato = ingresar_datos_campeonato()
    ingresar_equipos_y_jugadores(campeonato)
    campeonato.crear_jornadas()
    ingresar_resultados_juegos(campeonato)
    print("\nTabla de posiciones:")
    campeonato.mostrar_tabla_posiciones()
    print("\nEstadísticas de los jugadores:")
    campeonato.mostrar_estadisticas_jugadores()
    print(f"\nEl equipo campeón es: {campeonato.obtener_equipo_campeon()}")

if __name__ == "__main__":
    main()
