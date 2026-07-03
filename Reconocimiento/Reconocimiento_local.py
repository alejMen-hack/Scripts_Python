import sys
import os

if len(sys.argv) == 3:
    ruta = sys.argv[1]
    palabra_clave = sys.argv[2]
    iteracion = 0
    for root, dirs, files in os.walk(ruta):
         for archivo in files:
            if archivo.endswith((".txt", ".conf", ".env")):
                try:
                    with open(os.path.join(root,archivo), encoding="UTF-8", errors="ignore")as arch:
                        for linea in arch:
                            if palabra_clave in linea:
                                print(f"Se encontro un archivo con la palabra clave {palabra_clave} en la ruta:\n{root}\nEl archivo se llama: {archivo}\nLa linea en la que está es: {linea.strip()}\n")
                                print("=========================================================================================================================================\n")
                except PermissionError:
                    pass
