import os,sys
os.system("clear && figlet hi world")
a = input("  Enter the starting number : ")
print ""
b = input("  Enter the last number : ")
print ""
c = raw_input("  Enter Password List file : ")
os.system("clear")

while True :
	print a
	a += 1
	if a == b + 1 :
		sys.exit("Password List successfully")
	os.system("echo %s >> %s" %(a,c))
