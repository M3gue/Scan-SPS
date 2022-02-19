import os
from time import sleep
from PIL import Image

def Rename_func():    
    path = input("\nIngrese la ubicación de la carpeta para borrar COPIA: ")
    path = path.replace("\\","/") # Cambiamos los backslashes a slashes

    list_name = os.listdir(path) # Lista de todos los archivos del path
    # list_name.remove("Rename.py") # Eliminamos el nombre del script para que no pase nada malo

    new_list = [] # Almacenaremos la lista de los archivos
    new_list_updated = [] # Almacenaremos la lista de los archivos con los nombres cambiados

    # old_name = input("Ingrese las palabras que desea reemplazar:") # Nombre que va a buscar para reemplazar
    # new_name = input("Ingrese las palabras por las que se van a reemplazar:") # Nombre con el que lo va a reemplazar

    old_name = " copia" # Nombre que va a buscar para reemplazar
    new_name = "" # Nombre con el que lo va a reemplazar

    print("\nCreando lista con los nombres a cambiar...")
    for i in range(len(list_name)):
        if old_name in list_name[i]:
            new_list.append(list_name[i])
            
        sleep(0.02)

    print("\nCreando lista con los nombres cambiados...")
    new_list_updated = [name.replace(old_name, new_name) for name in new_list]

    print(f"\nCambiando los nombres de {len(new_list)} archivos...")

    total = len(new_list_updated)
    for i in range(len(new_list)):
        os.rename(path+"/"+new_list[i], path+"/"+new_list_updated[i]) # Renombramos el archivo en el path
        
        total -= 1
        print(f"{total} archivos restantes...")
        
        sleep(0.02)

    print("\n*** Proceso terminado ***")

def Rename_func_perso():    
    path = input("\nIngrese la ubicación de la carpeta para borrar MODIFICAR: ")
    path = path.replace("\\","/") # Cambiamos los backslashes a slashes

    list_name = os.listdir(path) # Lista de todos los archivos del path
    # list_name.remove("Rename.py") # Eliminamos el nombre del script para que no pase nada malo

    new_list = [] # Almacenaremos la lista de los archivos
    new_list_updated = [] # Almacenaremos la lista de los archivos con los nombres cambiados

    old_name = input("Ingrese las palabras que desea reemplazar:") # Nombre que va a buscar para reemplazar
    new_name = input("Ingrese las palabras por las que se van a reemplazar:") # Nombre con el que lo va a reemplazar

    print("\nCreando lista con los nombres a cambiar...")
    for i in range(len(list_name)):
        if old_name in list_name[i]:
            new_list.append(list_name[i])
            
        sleep(0.02)

    print("\nCreando lista con los nombres cambiados...")
    new_list_updated = [name.replace(old_name, new_name) for name in new_list]

    print(f"\nCambiando los nombres de {len(new_list)} archivos...")

    total = len(new_list_updated)
    for i in range(len(new_list)):
        os.rename(path+"/"+new_list[i], path+"/"+new_list_updated[i]) # Renombramos el archivo en el path
        
        total -= 1
        print(f"{total} archivos restantes...")
        
        sleep(0.02)

    print("\n*** Proceso terminado ***")

def Quitar_cero_func():
    path = input("\nIngrese la ubicación de la carpeta para eliminar CERO: ")
    path = path.replace("\\","/") # Cambiamos los backslashes a slashes

    list_name = os.listdir(path) # Lista de todos los archivos donde se encuentra nuestro script
    # list_name.remove("Quitar_Cero.py") # Eliminamos el nombre del script para que no pase nada malo

    list_name_updated = [] # Almacenaremos la lista de los archivos con los nombres cambiados
    
    print("\nCreando lista con los nombres cambiados...")
    list_name_updated = [name[1:] for name in list_name]
        
    print(f"\nCambiando los nombres de {len(list_name)} archivos...")
    total = len(list_name)
    for i in range(len(list_name)):
        os.rename(path+"/"+list_name[i], path+"/"+list_name_updated[i]) # Renombramos el archivo en el path
        
        total -= 1
        print(f"{total} archivos restantes...")
    
        sleep(0.02)
    
    print("\n*** Proceso terminado ***")
    
def Convert_func():
    path = input("\nIngrese la ubicación de la carpeta para CONVERTIR archivos: ")
    path = path.replace("\\","/") # Cambiamos los backslashes a slashes

    list_name = os.listdir(path) # Lista de todos los archivos del path

    folder = path + "/Converted" 
    os.makedirs(folder) # Creamos carpeta para las imágenes convertidas 

    total = len(list_name)
    
    print(f"\nConvirtiendo {total} archivos...")

    for filee in list_name:
        filename, extension = os.path.splitext(filee)
        
        im = Image.open(path + "/" + filename + extension)
        im.save(folder + "/" + filename + ".png")
        
        total -=1 
        print(f"{total} archivos restantes...")
        
        sleep(0.02)
  
    print("\n*** Proceso terminado ***")
    
x = input("Seleccione una opción:\n 1. Quitar COPIA. \n 2. MODIFICAR palabra \n 3. Quitar CERO. \n 4. Reconvertir archivos.\n\n")

if x == "1":
    Rename_func()
    
elif x == "2":
    Rename_func_perso()
    
elif x == "3":
    Quitar_cero_func()
    
elif x == "4":
    Convert_func()
    
else:
    print("Error, numero ingresado no válido")
    
input("\nPresione ENTER para continuar")
