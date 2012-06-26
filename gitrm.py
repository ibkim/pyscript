import os, sys

file = open("rmfiles.txt")

for line in file.readlines():
	file = line.split()[1]
	os.system("git rm " + file)

exit(0)
