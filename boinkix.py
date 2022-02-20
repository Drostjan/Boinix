from directory import *

root = Directory("/")
root.dir_add(Directory("bin"))
root.dir_add(Directory("etc"))
root.dir_add(Directory("usr"))
root.dir_add(Directory("tmp"))
root.dir_add(Directory("var"))
root.dir_add(Directory("opt"))
root.dir_add(Directory("home"))
clearConsole = lambda: print('\n' * 100)

def start():
    path = "/"
    print("\n **Boinikix v0.8:Beta** \n")
    keepRun = True
    while keepRun:
        starts = "\bboinix@boinix:"+path+"~$ "
        command = input(starts)
        cd = command.split(" ")

        if cd[0] == "salir":
            keepRun = False

        elif cd[0] == "ayuda":
            print("")
            print("====== Menu de ayuda ======          ")
            print("andestoy      - Indicará carpeta     ")
            print("cambiar       - Cambiar carpeta      ")
            print("salir         - Salir de la terminal ")
            print("creardir      - Crear carpeta        ")
            print("borrardir     - Borra carpeta        ")
            print("atrib         - Cambiar atributos    ")
            print("limpiar       - Limpiar pantalla     ")
            print("")

        elif cd[0] == "andestoy":
            print(path)

        elif cd[0] == "cambiar":
            if len(cd) == 1:
                path = path
            elif len(cd) == 2:
                if cd[1] == ".":
                    path = path
                elif cd[1] == "-" or cd[1] == "..":
                    if path == "/":
                        path = path
                    else:
                        p = path.split("/")
                        if len(p) == 2:
                            path = "/"
                        else:
                            path = "/" + p[1]
                elif "/" in cd[1]:
                    p = cd[1].split("/")
                    if p[1] in root.in_dir(p[1]):
                        path =  cd[1]
                    else:
                        print("Error: '%s'" % cd[1]," Ruta incorrecta.")
                else:
                    if cd[1] in root.in_dir(cd[1]):
                        path = "/" + cd[1]
                    else:
                        print("Error: '%s'" % cd[1]," Ruta incorrecta.")
                    
            else:
                print("Error: '%s'" % cd[1]," Ruta incorrecta.")
                
        elif cd[0] == "creardir":
            if path == "/":
                if "/" in cd[1]:
                    p = cd[1].split("/")
                    root.dir_add(p[1])
                else:
                    root.dir_add(cd[1])
            else:
                if "/" in cd[1]:
                    p = cd[1].split("/")
                    root.dir_add(p[1])
                else:
                    root.dir_add(cd[1])
            
        elif cd[0] == "borrardir":
            if path == "/":
                if "/" in cd[1]:
                    p = cd[1].split("/")
                    root.dir_remove(p[1])
                else:
                    root.dir_remove(cd[1])
            else:
                if "/" in cd[1]:
                    p = cd[1].split("/")
                    root.dir_remove(p[1])
                else:
                    root.dir_remove(cd[1])               
        
        elif cd[0] == "atrib":
            if cd[1] == "dir":
                pront = str(cd[2]) + "  -"
                if "W" in cd[3] or "w" in cd[3]:
                    pront = pront + str(cd[3]) 
                elif "R" in cd[3] or "r" in cd[3]:
                    pront = pront + str(cd[3])
                elif "X" in cd[3] or "x" in cd[3]:
                    pront = pront + str(cd[3])    
                else:
                    print("Error: '%s'" % cd[3],"Permiso incorrecto.") 
            elif cd[1] == "file":
                pront = str(cd[2]) + "  -"
                if "W" in cd[3] or "w" in cd[3]:
                    pront = pront + str(cd[3]) 
                elif "R" in cd[3] or "r" in cd[3]:
                    pront = pront + str(cd[3])
                elif "X" in cd[3] or "x" in cd[3]:
                    pront = pront + str(cd[3])
                    print(pront)
                else:
                    print("Error: '%s'" % cd[3],"Permiso incorrecto.") 
            else:
                print("Error: '%s'" % cd[1],"Tipo incorrecto.")
            
            print(pront)

        elif cd[0] == "touch":
            if len(cd) == 1:
                print("Error : Especifica el archivo.")
            elif len(cd) == 2:
                root.file_add(cd[1])
            else:
                root.file_add(cd[1])
                root.writeFile(cd[2:])

        
        elif cd[0] == "borrafile":
            root.file_remove(cd[1])

        elif cd[0] == "verrfile":
            read = root.readFile(cd[1])
            print(read)

        elif cd[0] == "tree":
            name = root.get_name()
            print(name,end='')
            print(" ",root.element())
           
        elif cd[0] == "limpiar":
            clearConsole()

        elif cd[0] == "sys":
            print("  S.O : Boinix v0.5 Alpha")
            print("  CMD : Boinikix v0.8:Beta\n")
        
        elif cd[0] == "":
            pass
        else:
            print("Error: '%s'" % cd[0],"command not found")
            pass

start()