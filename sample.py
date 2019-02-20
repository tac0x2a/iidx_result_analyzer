
# %%
import json as j

# %%

#%%
f = open("hoge2.json", encoding="utf-8") # sIMG_20190220_181356.jpg
# f = open("hoge.json", encoding="utf-8") # sIMG_20190220_181356.jpg
json = j.load(f)
text = json['textAnnotations']

s = text[0]
desc = s['description']
descs = desc.split('\n')
# print(desc)
# print("----------------------------")
print(descs)

def nearlest_label(labels, target):
    import difflib as dl
    return max(labels, key=lambda l: dl.SequenceMatcher(None, l, target).ratio())

import re
def clear_lamp(line, side=1):
    lamps = ['F-COMBO', 'EXH-CLEAR', 'H-CLEAR', 'CLEAR', 'E-CLEAR', 'A-CLEAR', 'FAILED']
    line = line.replace("CLEAR TYPE", "")
    line = line.replace("|", " ").strip()
    line = re.sub(r'\s+', " ", line)
    if side == 1:
        before, after = line.split(" ")
    else:
        after, before = line.split(" ")
    return nearlest_label(lamps, after)

def dj_level(line, side=1):
    levels = ['AAA', 'AA', 'A', 'B', 'C', 'D', 'E', 'F']
    line = line.replace("DJ LEVEL", "")
    line = line.replace("|", " ").strip()
    line = re.sub(r'[^ABCDEF]+', " ", line).strip()
    line = re.sub(r'\s+', " ", line)
    if side == 1:
        before, after = line.split(" ")
    else:
        after, before = line.split(" ")
    return nearlest_label(levels, after)

def parse_twin_number(line, digit=4):
    line = re.sub(r'[oOD]', "0", line).strip()
    line = re.sub(r'[lL]',  "1", line).strip()
    line = re.sub(r'[+-].+', "", line).strip()
    line = re.sub(r'\s+', "", line).strip()

    splited = []
    tmp = ""
    for c in line:
        if c.isdigit():
            tmp += c
        if len(tmp) >= digit:
            splited.append(tmp)
            tmp = ""

    if len(tmp) > 0:
        splited.append(tmp)

    return splited

def ex_score(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("EX SCORE", "")
    line = line.replace("|", " ").strip()
    splited = parse_twin_number(line, 4)
    if side == 1:
        before, after = splited
    else:
        after, before = splited
    return after

print("---------------------------------")
doc = {}
i = 1
while i < len(descs):
    line = descs[i]
    if line.startswith("CLEAR"):
        doc['lamp'] = clear_lamp(line)
    if line.startswith("DJ"):
        doc['dj_level'] = dj_level(line)
    if line.startswith("EX"):
        doc['ex_score'] = ex_score(line)
    i += 1

print(doc)

#%%
