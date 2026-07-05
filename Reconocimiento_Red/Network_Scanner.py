import sys
import os
import subprocess
import ipaddress
from colorama import init, Fore, Style

init(autoreset=True)

if len(sys.argv) == 2:
    try:
        red = sys.argv[1]
        ip_completa = ipaddress.ip_network(red,strict=False)
        print(f"\n{Fore.YELLOW}Iniciando el escaneo de la red: {red}\n")
        for ip in ip_completa.hosts():
            ip_str = str(ip)
            comando = ["ping", "-n", "1", "-w", "500", ip_str]
            resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if resultado.returncode == 0:
                print(f"{Fore.GREEN}[+] El host {ip_str} respondio!\n")
            else:
                continue
    except ValueError:
        print(f"\n{Fore.RED}El formato de red o máscara no es válido\n")