Para hacer uso de este Script se debe de tener un archivo en formato .txt que tenga la siguiente estructura:

- usuario,ip,intentos_Log
- usuario,ip,intentos_Log
- usuario,ip,intentos_Log

Teniendo este archivo se ejecuta en consola el siguiente comando: python Analizador_Logs.py archivo.txt 3
En el comando anterior el numero 3 corresponde al numero de intentos que queremos aceptar, de modo que si supera este numero se considera un intento de acceso ilegal y se quiere tener su IP para bloquearla en el Firewall
