import sys
import os 
import socket
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import init, Fore, Style

def escanear_puerto(puerto):
    port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port.settimeout(0.5)
    resultado_puerto = port.connect_ex((ip_address,puerto))
    if resultado_puerto == 0:
        try:
            servicio = socket.getservbyport(puerto)
            print(f"\n{Fore.GREEN}[+] Puerto: {puerto} abierto ---> Servicio: {servicio}\n")
        except OSError:
            print(f"\n{Fore.GREEN}[+] Puerto: {puerto} abierto ---> Servicio: desconocido\n")
    else:
        pass

if len(sys.argv) == 4:
    try:
        ip_address = sys.argv[1]
        primer_puerto = int(sys.argv[2])
        ultimo_puerto = int(sys.argv[3])
        with ThreadPoolExecutor(max_workers=100) as ejecutar:
            puertos = range(primer_puerto,ultimo_puerto+1)
            ejecutar.map(escanear_puerto, puertos)
    except:
        print(f"\n{Fore.RED}No esta funcionando\n")