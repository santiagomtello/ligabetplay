import modules.menus as mn
import modules.msgerror as msgE
import modules.agregar as agg
import modules.ver as see
import modules.exit as ex
import os

def plantelmenu(equipos):
    try:
        isplantelmenu=True
        print(mn.menuplantel)
        opcmenuplantel= int(input('Elija la opcion a la que desea acceder: '))
        os.system('cls')
        match opcmenuplantel:
            case 1:
                agg.addjugadores(equipos)
                os.system('cls')
            case 2:
                agg.addplantel(equipos)
                os.system('cls')
            case 3:
                see.mirarjugadores(equipos)
            case 4:
                isplantelmenu=ex.exitOpcion
            case _:
                msgE.opcnovalid
    except ValueError:
        msgE.opcnovalid