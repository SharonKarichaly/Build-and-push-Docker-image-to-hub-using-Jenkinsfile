import socket
import subprocess

hostname=socket.gethostname()
print("Hostname of the machine =" ,hostname)
print()

ip = socket.gethostbyname(hostname)
print("IP of the machine =",ip)
print()

memory = subprocess.check_output("grep MemTotal /proc/meminfo | awk '{print $2,$3}'", shell=True, universal_newlines=True)
print("Total available memory of the machine=", memory)
load = subprocess.check_output("uptime | awk '{print $8,$9,$10}'", shell=True, universal_newlines=True)
print("Load average of the machine=",load)
diskusage = subprocess.check_output("df -h | awk 'NR>=0 && NR<=2'", shell=True, universal_newlines=True)
print("disk usage of the machine=", diskusage)
