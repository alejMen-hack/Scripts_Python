import sys

if len(sys.argv) == 3:
    arch = sys.argv[1]
    limite_intentos = sys.argv[2]
    try:
        with open(arch, encoding="UTF-8") as archivo:
            iteracion = 0
            contadorFallido = 0
            conteo_Fallos = {}

            for linea in archivo:
                # line = archivo.readline()
                iteracion += 1
                line = linea.strip().split(",")

                usuario = line[0]
                ip = line[1]
                estado = line[2]
                # print (f"Linea {iteracion}: ",linea)
                if ip not in conteo_Fallos and estado == "FALLIDO":
                    conteo_Fallos[ip] = 1
                elif ip in conteo_Fallos and estado == "FALLIDO":
                    conteo_Fallos[ip] += 1
                else:
                    continue
                
            with open("ips_bloqueadas.txt", "w") as n_Archivo:
                for clave, valor in conteo_Fallos.items():
                    if valor >= limite_intentos:
                        n_Archivo.write(f"{clave}\n")
    
    except FileNotFoundError:
        print(f"[-] Error Crítico: El archivo '{arch}' no fue encontrado. Verifica la ruta.")

    # Si el usuario pone una letra en vez de un número en el límite, int() fallará y lanzará ValueError:
    except ValueError:
        print("[-] Error: El límite de intentos debe ser un número entero. Ejemplo: 3")

    # Captura cualquier otro error inesperado (permisos, archivos corruptos, etc.)
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado: {e}")

            

