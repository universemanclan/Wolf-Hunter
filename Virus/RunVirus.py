import time

dir_path = os.path.dirname(os.path.realpath(__file__))

workingdir = os.getcwd()

Virus = dir_path+"Virus.py"

time.sleep(5)
exec(open(Virus).read())

time.sleep(4)

exit()
