import subprocess
import sys
import os 
import getpass

# This is a simple tool used to initiate HTB or any other CTF 

help_manual = (
    "This is a very simple but useful tool :)\n"
    "-----------------------------------------" 
    "\nSTART VPN = sv"
    "\nStart Windows connection"
)

# Get current machine/host name
user = getpass.getuser()

# This is used for manual or invalid syntax
if len(sys.argv) < 2:
    print("--> no argv given (if you need help press 'h' or 'help')")

if sys.argv[1] == "help" or "h":
    print(help_manual)


# Check for for vpn files and output error if file is not found.
try:
    if sys.argv[1] == "sv":
        conn_type = str(input("What connection type ?\n udp = u\n tcp = t\n--->")) 

        if conn_type.lower() == "u" or "udp":
            subprocess.Popen(["openvpn", f"/home/{user}/openvpn_files/udp_academy.ovpn", "-y"])
        elif conn_type.lower() == "t" or "tcp":
            subprocess.Popen(["openvpn", f"/home/{user}/openvpn_files/tcp_academy.ovpn", "-y"])

except subprocess.CalledProcessError:
    print("\033[31mError on path\033[0m")
