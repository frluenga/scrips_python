from os import close
import re

pattern = re.compile(r'^([\d]{4,4})\-.*,(Friendly,.*)$')

with open('./results.csv','r',encoding='UTF-8') as f:
    for line in f:
        res = re.match(pattern,line)
        if res:
            print(f'{res.group(1)} {res.group(2)}\n')
    f.close()
