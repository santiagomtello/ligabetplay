import modules.menus as mn
import modules.msgerror as msgE
import modules.equipos as Requipos
import modules.plantel as Rplantel
import modules.agregar as agg
import modules.ver as see
import modules.exit as ex
import os

equipos=[]
fechas=[]

def menu():
    try:
        isactive=True
        global equipos, fechas
        while isactive:
            print(mn.menuprinciplal)
            opcmenuprincial = int(input('Elija la opcion a la que desea acceder: '))
            os.system('cls')
            match opcmenuprincial:
                case 1:
                    Requipos.equiposmenu(equipos)
                case 2:
                    Rplantel.plantelmenu(equipos)
                case 3:
                    agg.addfecha(equipos,fechas)
                case 4:
                    see.verResultados()
                case 5:
                    isactive = ex.exitOpcion
                case _:
                    msgE.opcnovalid
    except ValueError:
        msgE.opcnovalid