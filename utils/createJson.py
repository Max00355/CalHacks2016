import json
import re
import pprint

builtJson = {}
html = open("test.txt", 'r').read().replace("\n", "")

airports = html.split('</tr><tr bgcolor="#d1d1d1">')

for a in airports:
    tags = re.findall("</\w+>", a) + re.findall("<\w+>", a)
    for t in tags:
        a = a.replace(t, ' ')
    raw = a.split()
    for i,x in enumerate(raw):
        if len(x) == 2:
            break
    state = ' '.join(raw[:i]).lower()
    builtJson[state] = {}
    formatted = raw[i+1:]
    fullName = ""
    for f in formatted:
        f = f.replace(" ", '').replace("\n", "")
        if len(f) != 3 or f[1].islower():
            fullName += f + " "
        else:
            fullName, abrev = ' '.join(fullName.replace("\n", "").split()), f.replace(" ", '').replace("\n", '')
            print fullName, abrev
            builtJson[state][fullName] = abrev
            fullName = ""

json.dump(builtJson, open("airportsJson.json", 'w'))

