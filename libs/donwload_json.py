#!/usr/bin/env python2
import urllib as ur
import pwd,os,sys
user=pwd.getpwuid(os.getuid())[0]
sys.path.append("/home/" + user + "/bin/MinecraftLauncher/Python/libs") 
import constants,log
log.main("Dowloading list file")
ur.urlretrieve(constants.JSON_URL, constants.JSON_PATH)
if os.path.isfile(constants.JSON_PATH):
	log.main("Done!")
	log.main("List Path: " + constants.JSON_PATH)
else:
	log.main("Can't download file.")
	sys.exit(1)
#end