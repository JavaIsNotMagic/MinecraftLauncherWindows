import os,pwd
username=pwd.getpwuid(os.getuid())[0]
home_dir="/home/" + username
root_dir = home_dir + "/bin/MinecraftLauncher/Python"
JSON_PATH=root_dir+ "/data/list.json"
JSON_URL="https://launchermeta.mojang.com/mc/game/version_manifest.json"