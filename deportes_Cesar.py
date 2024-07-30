from tabulate import tabulate

class Persona:
    def __init__(self, nombre, id, sexo, fecha_nacimiento):
        self.nombre = nombre
        self.id = id
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento


class Jugador(Persona):
    def __init__(self, nombre, id, sexo, fecha_nacimiento, equipo, id_jugador):
        super().__init__(nombre, id, sexo, fecha_nacimiento)
        self.equipo = equipo
        self.id_jugador = id_jugador


class Equipo:
    def __init__(self, id_equipo, nombre_equipo):
        self.id_equipo = id_equipo
        self.nombre_equipo = nombre_equipo
        self.jugadores = []
        self.puntos = 0

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} ({jugador.id_jugador})")

    def agregar_puntos(self, puntos):
        self.puntos += puntos


class Estadisticas:
    def __init__(self):
        self.marcador = 0
        self.victoria = 0
        self.empate = 0
        self.perdido = 0

    def registrar_empate(self, marcador):
        self.marcador = marcador
        self.empate += 1


class TablaPosicion:
    def __init__(self):
        self.posiciones = {}

    def actualizar_posicion(self, equipo):
        self.posiciones[equipo.nombre_equipo] = equipo.puntos

    def mostrar_tabla(self):
        print("Tabla de Posiciones:")
        tabla = [[equipo, puntos] for equipo, puntos in sorted(self.posiciones.items(), key=lambda item: item[1], reverse=True)]
        print(tabulate(tabla, headers=["Equipo", "Puntos"], tablefmt="grid"))


class Campeonato:
    def __init__(self, premio, campeon):
        self.premio = premio
        self.campeon = campeon
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_equipos(self):
        for equipo in self.equipos:
            print(f"Equipo: {equipo.nombre_equipo}")
            equipo.mostrar_jugadores()


class CalendarioDeportivo:
    def __init__(self, fecha_inicial, fecha_final):
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.campeonatos = []

    def iniciar_campeonato(self):
        print("Campeonato iniciado")

    def agregar_campeonato(self, campeonato):
        self.campeonatos.append(campeonato)

    def mostrar_campeonatos(self):
        for campeonato in self.campeonatos:
            print(f"Campeonato: {campeonato.premio}, Equipos:")
            campeonato.mostrar_equipos()


def crear_jugador(equipo):
    nombre = input("Nombre del jugador: ")
    id = input("ID del jugador: ")
    sexo = input("Sexo del jugador (M/F): ")
    fecha_nacimiento = input("Fecha de nacimiento del jugador (YYYY-MM-DD): ")
    id_jugador = int(input("ID del jugador en el equipo: "))
    return Jugador(nombre, id, sexo, fecha_nacimiento, equipo, id_jugador)


def crear_equipo(id_equipo):
    nombre_equipo = input("Nombre del equipo: ")
    equipo = Equipo(id_equipo, nombre_equipo)
    num_jugadores = int(input("Numero de jugadores en el equipo: "))
    for _ in range(num_jugadores):
        jugador = crear_jugador(nombre_equipo)
        equipo.agregar_jugador(jugador)
    return equipo


def registrar_empate(estadisticas):
    marcador = int(input("Ingrese el marcador del empate [2-2]: "))
    estadisticas.registrar_empate(marcador)


def registrar_partido(equipo1, equipo2, goles_equipo1, goles_equipo2):
    if goles_equipo1 > goles_equipo2:
        equipo1.agregar_puntos(3)
    elif goles_equipo1 < goles_equipo2:
        equipo2.agregar_puntos(3)
    else:
        equipo1.agregar_puntos(1)
        equipo2.agregar_puntos(1)


def main():
    equipos = []
    num_equipos = int(input("Numero de equipos: "))

    for i in range(1, num_equipos + 1):
        equipo = crear_equipo(i)
        equipos.append(equipo)

    campeonato = Campeonato("Premio de Campeonato", "Campeon del Campeonato")
    for equipo in equipos:
        campeonato.agregar_equipo(equipo)

    calendario = CalendarioDeportivo("2023-01-01", "2023-12-31")
    calendario.agregar_campeonato(campeonato)
    calendario.iniciar_campeonato()

    for i in range(len(equipos)):
        for j in range(i + 1, len(equipos)):
            print(f"Partido entre {equipos[i].nombre_equipo} y {equipos[j].nombre_equipo}")
            goles_equipo1 = int(input(f"Ingresa los goles del {equipos[i].nombre_equipo}: "))
            goles_equipo2 = int(input(f"Ingresa los goles del {equipos[j].nombre_equipo}: "))
            registrar_partido(equipos[i], equipos[j], goles_equipo1, goles_equipo2)

    tabla_posicion = TablaPosicion()
    for equipo in equipos:
        tabla_posicion.actualizar_posicion(equipo)

    calendario.mostrar_campeonatos()
    tabla_posicion.mostrar_tabla()


if __name__ == "__main__":
    main()
