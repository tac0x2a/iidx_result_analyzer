
# %%
import json as j

# %%

#%%
# f = open("hoge2.json", encoding="utf-8") # sIMG_20190220_181356.jpg
f = open("hoge.json", encoding="utf-8") # sIMG_20190220_181356.jpg
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

print("---------------------------------")
doc = {}
i = 1
while i < len(descs):
    line = descs[i]
    if line.startswith("CLEAR"):
        doc['lamp'] = clear_lamp(line)
    if line.startswith("DJ"):
        doc['dj_level'] = dj_level(line)
    i += 1

print(doc)

#%%
