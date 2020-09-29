#!/usr/bin/env python3
from scan_print import scan
from get_ip import get_ip_addr
from intro import intr
intr()
lhost=get_ip_addr()

print("\u001b[42m \u001b[30;1m ENTER THE TIME DURATION IN SECONDS TO WAIT FOR RESPONSE \u001b[0m","OR","\u001b[30;1m \u001b[41m PRESS ENTER TO SET DEFAULT VALUE i.e 10 seconds \u001b[0m")
print("\n\u001b[31;1m [Note]--> You can change the value of time duration according to number of packets.\u001b[0m")
time = str(input(">>"))
time = time.strip()
if not time:
    print("\u001b[33;1m \u001b[47m[!]YOU DID NOT PROVIDE THE TIME DURATION SO SETTING TO DEFAULT\u001b[0m")
    time = "10"
user_time = time.isnumeric()
while (user_time!=True):
    print("\u001b[47m \u001b[31;1m [X] oops!! that does not seem to be a time format please try again \u001b[0m")
    time1=input(">>")
    user_time = time1.isnumeric()
    time=time1
scan(lhost,int(time))
print("\n")

