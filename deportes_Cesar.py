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

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} ({jugador.id_jugador})")


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

    def actualizar_posicion(self, equipo, puntos):
        self.posiciones[equipo.nombre_equipo] = puntos

    def mostrar_tabla(self):
        print("Tabla de Posiciones:")
        for equipo, puntos in self.posiciones.items():
            print(f"Equipo: {equipo}, Puntos: {puntos}")


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
    marcador = int(input("Ingrese el marcador del empate  [2-2]: "))
    estadisticas.registrar_empate(marcador)


def main():

    equipoA = crear_equipo(1)
    equipoB = crear_equipo(2)

    campeonato1 = Campeonato("Premio1", "Campeon1")
    campeonato1.agregar_equipo(equipoA)

    campeonato2 = Campeonato("Premio2", "Campeon2")
    campeonato2.agregar_equipo(equipoA)
    campeonato2.agregar_equipo(equipoB)
    calendario = CalendarioDeportivo("2023-01-01", "2023-12-31")
    calendario.agregar_campeonato(campeonato1)
    calendario.agregar_campeonato(campeonato2)
    calendario.iniciar_campeonato()
    estadisticas = Estadisticas()
    registrar_empate(estadisticas)
    tabla_posicion = TablaPosicion()
    tabla_posicion.actualizar_posicion(equipoA, 1)
    tabla_posicion.actualizar_posicion(equipoB, 2)

    calendario.mostrar_campeonatos()
    print(f"Empate registrado: {estadisticas.marcador}-{estadisticas.marcador}")
    tabla_posicion.mostrar_tabla()


if __name__ == "__main__":
    main()
