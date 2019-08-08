#log.py
import pwd,os,sys
from datetime import datetime as dt
date = dt.now().strftime("%m-%d-%y")
user=pwd.getpwuid(os.getuid())[0]
sys.path.append("/home/" + user + "/bin/MinecraftLauncher/Python/libs") 
import constants
#MAIN
def main(input):
	logfile = constants.root_dir + "/data/logs/" + date + ".log"
	f = open(logfile, "a+")
	f.write(input)
	f.write(os.linesep)
	f.flush()
	f.close()
#end