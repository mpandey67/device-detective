import re
import subprocess
def get_ip_addr():
    i=0
    ifconfig_output=subprocess.check_output(["ifconfig"])
    lhost=re.search(r"\W*(inet)W*\s\d\d\d.\d\d\d.\d[0-9]*.",str(ifconfig_output))
    if not lhost:
        print("\ncheck your internet connection. CONNECT TO A NETWORK")
        print("EXITING...")
        exit()
    lhost = lhost.group(0).strip(' ')
    lhost = lhost[5:]
    lhost = lhost + "1/24"
    print("\nyour local ip range is: " "\u001b[32;1m"+lhost+ "\u001b[0m" "\u001b[37;1m  using this ip for scanning\n \u001b[0m")
    print("\u001b[32;1m enter the IP range of your choice else hit enter for what I detected on your device  " +lhost+ "\u001b[0m")
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    user_lhost=input(">>")
    user_lhost=user_lhost.strip(' ')
    if not user_lhost:
        print("setting your ip to " + lhost)
        user_lhost=lhost
        return user_lhost
    if re.search(regex,user_lhost):
        user_lhost = user_lhost.split('.')
        user_lhost1 = ""
        while i < 3:
            user_lhost1 = user_lhost1 + user_lhost[i] + '.'
            i = i + 1

        user_lhost1 = user_lhost1+"1/24"
        print("setting you ip range to " + user_lhost1)
        return user_lhost1
    else:
        print("\u001b[31m ERROR: Network range must be 0.0.0.0 I WILL AUTOMATICALLY USE IT IN ENTIRE SUBNET \u001b[0m")
        print("\u001b[32m Run the tool again \u001b[0m")
        print("\u001b[33;1m EXITING... \u001b[0m")
        exit()
