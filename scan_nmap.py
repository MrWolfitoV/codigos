#Python3 code for scanning with  nmap 


#Librerias 

import os
import time
import subprocess

#Variables

IP=input("IP a escanear : ")

IR_IP=("0.0.0.0")

hostname = IP

r = os.system("ping -c 1 " + hostname)

#Procesos básicos

if IP != IR_IP:

        time.sleep(1)
        print(f"La IP seleccionada es : {hostname} \n")

        if r == 0:
                print(f"{hostname} funciona")

        else:
                print(f"{hostname} no funciona")

elif IR_IP:

        print("\n")
        print("Por favor vuelve a intentarlo")

if r == 0:

        print("\n")
        os.system('nmap -p- -sS --open --min-rate 5000 -n -vvv -Pn -oG allPorts' " " + hostname)
        print("\n ")

        print("El proceso a finalizado")
