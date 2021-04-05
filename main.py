import winreg
import time
import re


key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_READ)


def fetchPlayers():
    recentPlayers = winreg.QueryValueEx(key, "recentPlayers_h684323726")[0].decode('utf8')

    #pattern = re.compile(r"\"([0-9a-zA-Z\ \(\)\[\]\{\}\@]+)\"\,\"friend\_code\"\:\"([0-9a-zA-Z\ \(\)\[\]\{\}\@]+)\#(\d{4})\"")
    pattern = re.compile(r"\"([^\"]+)\"\,\"friend\_code\"\:\"([^\"]+)\#(\d{4})\"")


    return re.findall(pattern, recentPlayers)
    
        
oldPlayers = fetchPlayers()


while True:
    newPlayers = fetchPlayers()
    diff = set(newPlayers) - set(oldPlayers)
    if diff:
        for alias, name, code in diff: 
            print(alias, name + "#" + code)
    oldPlayers = newPlayers
    time.sleep(1)
