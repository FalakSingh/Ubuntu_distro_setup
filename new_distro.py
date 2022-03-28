import sys 
import subprocess 

args = str(sys.argv)
if not args:
	print("Provide Arguments")
sudo_command = "sudo apt install terminator wireshark htop net-tools python3-pip netdiscover gnome-tweaks aircrack-ng"
if args = "1":
	subprocess.call(sudo_command,shell=True)

