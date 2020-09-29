import subprocess
import getpass
import os

inp = getpass.getpass("Enter your password : ")
ipass = "user"

if inp != ipass:
    print("Password Incorrect. You can't login")
    exit()
    
cmd = input("Enter your Command : ")
x = subprocess.getstatusoutput(cmd)
status = x[0]
output = x[1]
if status == 0 :
    print(output)
else:
    print("Error in your command")    