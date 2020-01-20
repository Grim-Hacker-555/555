import os,sys
form time import sleep as t
os.system("figlet hi world")
t(0.6)
os.system("clear && figlet keren")
a = raw_input("Enter Starting number : ")
b = raw_input("Enter Ending number : ")
c = raw_input("Enter Pass List : ")
while True :
    print(a)
    a += 1
    if a == b :
        sys.exit()
    os.system("echo %s >> %s" %(a,c))
    else :
        os.system("figlet Error")
    
