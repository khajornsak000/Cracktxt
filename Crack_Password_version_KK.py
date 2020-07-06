import random
import sys

def note():
    print("<กรอกชื่อไฟล์หรือชื่อไฟล์และนามสกุลไฟล์> & <input name file> ")

def main(file):
    with open(file, "r") as files:
        passwd = str(files.read())
    password = ""
    while password != passwd:
        password= ""
        for i in range(len(passwd)):
           number = random.choice("0123456789abcdefghijklmnopqrsuvwyz")
           password += "".join(number)
           print("[*] Password = ", password)
    print("Password = ",password)

if len(sys.argv) != 2:
    note()
else:
    if sys.argv[1][-3:] == "txt":
         main(sys.argv[1])
    else:
        x = sys.argv[1]
        x+= ".txt"
        main(x)

    

