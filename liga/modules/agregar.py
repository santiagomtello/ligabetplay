import modules.ver as see
import modules.exit as ex
import os
import modules.fechaval as fech

def addequipos(equipos):
    nombre= input('Ingrese el nombre del equipo: ').strip()
    if not nombre:
        print('ingrese un nombre de equipo')
    elif any(nombre==equipo ['nombre'] for equipo in equipos):
        print(f'el equipo {nombre} ya existe')
    else:
        equipos.append({'nombre':nombre,
                    'jugadores':[],
                    'pantel':[]})
        print(f'el equipo {nombre} se ha creado exitosamente')
    mas= input('desea agregar otro equipo N(no) enter(si)')

    if (bool(mas)==False):
        addequipos(equipos)
    else:
        return equipos

def addjugadores(equipos):
    isaddjugadores=True
    while isaddjugadores:
        mirar=see.elegirequipos(equipos)
        N_equipos= len(equipos)
        if mirar>N_equipos or bool(mirar)==False:
            input('no se puede agregar, el equipo no existe')
            os.system('cls')
        else: 
            os.system('cls')
            nombreJugador= input('ingrese el nombre del jugador: ')
            os.system('cls')
            dorsal = input('ingrese numero de dorsal del jugador: ')
            os.system('cls')
            jugadorPosicion = input('ingrese la posicion del jugador: ')
            os.system('cls')
            
            jugador = {'nombre':nombreJugador,
                    'posicion': jugadorPosicion,
                    'dorsal':dorsal}
            equipos[mirar-1]['jugadores'].append(jugador)
            print('si no desea agregar mas jugadores, presione enter')
            isaddjugadores =ex.hacerMas

def addplantel(equipos):
    mirar=int(see.eliminarequiopo(equipos))
    N_equipos= len(equipos)
    if mirar>N_equipos or bool(mirar)==False:
        input('no es posible agregar, el equipo no existe')
        os.system('cls')
    else:
        nombre= input('ingrese el nombre del miembro del CT: ')
        os.system('cls')
        cargo = input('ingrese el cargo que ejerce: ')
        os.system('cls')
        
        jugador = {'nombre':nombre,
                'cargo': cargo}
        equipos[mirar-1]['plantel'].append(jugador)
        isaddjugadores =ex.hacerMas

def addfecha(equipos,fechas):
    isaddfecha=True
    while isaddfecha:
        print("""
            ELIJA EL EQUIPO 1
        """)
        equipo1= see.elegirequipos(equipos)
        equipo1 -=1
        os.system('cls')

        print("""
            ELIJA EL EQUIPO 2
        """)
        equipo2= see.elegirequipos(equipos)
        equipo2 -=1
        os.system('cls')

        if equipo1 < 0 or equipo1 >= len(equipos) or equipo2 < 0 or equipo2 >= len(equipos):
            input("Error: Equipo no encontrado")
            os.system('cls')
            return
        
        dia = int(input('Ingrese el día: '))
        mes = int(input('Ingrese el mes: '))
        año = int(input('Ingrese el año: '))
        fecha =(dia,mes,año)
        fech.fecha(dia,mes,año)
        os.system('cls')

        resultado = input("Ingrese el resultado del partido (Goles equipo 1 - Goles equipo 2): ")
        print(f"Partido agregado: {equipos[equipo1]['nombre']} vs {equipos[equipo2]['nombre']} - Fecha: {fecha} - Resultado: {resultado}")        
        if hasattr(addfecha, "fechas"):
            fechas = addfecha.fechas
        else:
            addfecha.fechas = []
        
        fechas.append({
        "equipo1": equipos[equipo1]['nombre'],
        "equipo2": equipos[equipo2]['nombre'],
        "fecha": fecha,
        "resultado": resultado
        })

        isaddfecha = ex.hacerMas()
        addfecha.fechas = fechas


def deleteequipo(equipos):
    mirar=int(see.eliminarequiopo(equipos))
    N_equipos= len(equipos)
    if mirar>N_equipos or bool(mirar)==False:
        input('no existe ningun equipo para eliminar')
        os.system('cls')
    else:
        os.system('cls')
        equipos.pop(mirar-1)
    os.system('cls')
