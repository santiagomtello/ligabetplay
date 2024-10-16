import os
import modules.agregar as agg

def mirarequipos(equipos):
    if equipos:
        print ('equipos disponibles')
        for i, equipo in enumerate(equipos,start=1):
            print (f'{i}:{equipo['nombre']}')
        print('')
    else:
        print('no hay equipos registrados')
    input('presione enter para salir')
    os.system('cls')

def elegirequipos(equipos):
    if equipos:
        print('equipos disponibles')
        for i,equipo in enumerate (equipos, start=1):
            print (f'{i}:{equipo['nombre']}')
        print('')
        eleccion= int(input('ingrese el numero del equipo que desea:'))
        return eleccion
    else:
        print('No hay equipos registrados')
        return False

def mirarjugadores(equipos):
    e = 0
    for i, equipo in enumerate(equipos, start=1):
        print(f"{i}.Equipo: {equipo['nombre']}")
        print("""
                JUGADORES
            """)
        for jugador in equipo['jugadores']:
            e=+1
            print(f"  {e} Nombre del jugador: {jugador['nombre']}")
            print(f"  - Posición: {jugador['dorsal']}")
            print(f"  - Número: {jugador['numero']}")
        print("""
                PLANTEL
            """)
        e = 0
        for plantel in equipo['plantel']:
            e=+1
            print(f"  {e}. nombre del {plantel['cargo']}: {plantel['nombre']}")
        print('')
    print('')
    print('presione para salir:')
    input('')

def verResultados():
    if hasattr(agg.addfecha, 'fechas'):
        fechas= agg.addfecha.fechas
        if fechas:
            print('fechas de partidos')
            for fecha in fechas:
                print (f'{fecha['equipo1']} vs {fecha['equipo2']} - fecha {fecha['fecha']} - resultado {fecha['resultado']}')
            input('')
        else:
            print('no hay fechas de partido agregadas')
            input('')
            os.system('cls')
    else:
            print('no hay fechas de partido agregadas')
            input('')
            os.system('cls')


def eliminarequiopo(equipos):
    if equipos:
        print('equipos actuales')
        for i,equipo in enumerate (equipos, start=1):
            print (f'{i}:{equipo['nombre']}')
        print('')
        delete= int(input('ingrese el numero del equipo que desea eliminar:'))
        return delete
    else:
        print('No hay equipos registrados')
        return False
