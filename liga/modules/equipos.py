import modules.menus as mn
import modules.msgerror as msgE
import modules.agregar as agg
import modules.ver as see
import modules.exit as ex
import os

def equiposmenu(equipos):
    try:
        ismenuequipos=True
        while ismenuequipos:
            print(mn.menuequipos)
            opcmenuequipos = int(input('Elija la opcion a la que desea acceder: '))
            os.system('cls')
            match opcmenuequipos:
                case 1:
                    agg.addequipos(equipos)
                    os.system('cls')
                case 2:
                    delete = agg.deleteequipo(equipos)
                case 3:
                    ver=see.mirarequipos(equipos)
                case 4:
                    ismenuequipos = ex.exitOpcion()
                case _:
                    msgE.opcnovalid
    except ValueError:
            msgE.opcnovalid