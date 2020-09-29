import scapy.all as scapy
import subprocess
from intro import intr
def scan(ip,time):
    ip_addr = scapy.ARP(pdst=ip)
    mac_addr = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ip_mac = mac_addr / ip_addr
    print("\n \u001b[31;1m \u001b[47m FETCHING YOUR CLIENTS......... PLEASE WAIT \u001b[0m" "\u001b[31;1m \u001b[47m" + str(time) + "\u001b[0m" "\u001b[31;1m \u001b[47m seconds \u001b[0m", end="\r")
    answered_packet = scapy.srp(ip_mac, timeout=time, verbose=False)[0]
    subprocess.call(["clear"])
    intr()
    print("----------------------------------------------------------")
    print("\u001b[31;1m \u001b[47m IP ADDRESS \t\t\t ASSOCIATED MAC \u001b[0m")
    print("----------------------------------------------------------\n")
    for elements in answered_packet:
        print(elements[1].psrc + "-------------------->" + elements[1].hwsrc)
    print("\u001b[32;1m Finished \n \u001b[0m")
    print("\u001b[31;1m [Note]--> You can change the value of time duration according to number of packets.\u001b[0m")
