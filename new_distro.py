import subprocess 
import sys
import os

args = sys.argv

help = """
[+] Use 1 for apt installations
[+] Use 2 for metasploit installation
[+] Use 3 for changing login background
[+] Use 4 for opening wayland custom conf file
[+] Use 5 for installing Mac theme
[+] Use 6 for copying Colloid theme in icons folder
[+] Use 7 for terminal and terminator config
[+] Use 'all' for executing every command at once
"""
cwd = os.getcwd()
if len(args) < 2:
    print("Please provide arguments")
    print(help)    

apt_command = "sudo apt install terminator wireshark htop net-tools python3-pip netdiscover gnome-tweaks aircrack-ng bleachbit curl git"
mfsconsole_command = "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall"
login_command = f'sudo bash login_bg_change.sh --image {os.getcwd()}/night.jpg'
gdm_path = "sudo gedit /etc/gdm3/custom.conf"
mac_theme = "unzip mac.zip && cd WhiteSur-gtk-theme-master && ./install.sh && ./install.sh -N glassy"
icon_theme = "mkdir .icons && tar -xvf 01-Colloid.tar.xz -C .icons && mv -f .icons ~/"
bash_command = "unzip distro_files.zip && cd distro_files && cp .bashrc .bash_aliases ~/ && cp config ~/.config/terminator/"

full_setup = f'''sudo apt install terminator wireshark htop net-tools python3-pip netdiscover gnome-tweaks aircrack-ng bleachbit curl git &&
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall &&
unzip mac.zip && cd WhiteSur-gtk-theme-master && ./install.sh && ./install.sh -N glassy && cd {cwd}
mkdir .icons && tar -xvf 01-Colloid.tar.xz -C .icons && mv -f .icons ~/ &&
unzip distro_files.zip && cd distro_files && cp .bashrc .bash_aliases ~/ && cp config ~/.config/terminator/ && cd {cwd}
sudo bash login_bg_change.sh --image {os.getcwd()}/night.jpg
'''
if len(args) == 2:
    if args[1] == "1":
        subprocess.call(apt_command, shell=True)
    if args[1] == "2":
        subprocess.call(mfsconsole_command, shell=True)
    if args[1] == "3":
        subprocess.call(login_command, shell=True)
    if args[1] == "4":
        subprocess.call(gdm_path, shell=True)
    if args[1] == "5":
        subprocess.call(mac_theme, shell=True)
    if args[1] == "6":
        subprocess.call(icon_theme, shell=True)
    if args[1] == "7":
        subprocess.call(bash_command,shell=True)

    if args[1] == "all":
        subprocess.call(full_setup, shell =True)

