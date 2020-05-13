import json
import os

file_path = "~/.mozilla/firefox/6d8rle6g.default-release/sessionstore-backups/recovery.jsonlz4"
os.system('python mozlz4a.py -d %s output.json' % file_path)
f = open("output.json", "r")

contents = json.load(f)

f.close()
for win in contents["windows"]:
    for tab in win["tabs"]:
        i = tab["index"] - 1
        print(tab["entries"][i]["url"])
