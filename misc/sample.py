
# %%
import json as j

# %%

#%%
f = open("hoge2.json", encoding="utf-8") # sIMG_20190220_181356.jpg
f = open("hoge.json", encoding="utf-8") # sIMG_20190220_181356.jpg
f = open("hoge3.json", encoding="utf-8") # sIMG_20190220_181356.jpg
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
    line = line.replace("|", " ")
    line = re.sub(r'\s+', " ", line)

    tmp = []
    s = ""
    for l in line.split(" "):
        if len(l) <= 1:
            s += l
        else:
            tmp.append(s + l)
    line = tmp

    if side == 1:
        before, after = line
    else:
        after, before = line
    return nearlest_label(lamps, after)

def num(s):
    s = s.strip()
    s = re.sub(r'[QoOםDם]', "0", s)
    s = re.sub(r'[lLןוו]',  "1", s)
    s = re.sub(r'[Uu]',  "4", s)
    s = re.sub(r'[Ss]',  "5", s)
    s = re.sub(r'[A]',  "8", s)
    s = re.sub(r'[q]',  "9", s)
    return s

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

def parse_number(line, digit=4, cnt=2):
    line = num(line)
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

    if len(splited) > cnt:
        splited = splited[0:cnt]
    return [int(d)  for d in splited]

def ex_score(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("EX SCORE", "")
    line = line.replace("|", " ").strip()
    splited = parse_number(line, 4, 2)
    if len(splited) <= 1:
        return splited[0] # first play ?

    if side == 1:
        before, after = splited
    else:
        after, before = splited
    return after

def miss_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("MISS COUNT", "")
    line = line.replace("|", "").strip()
    splited = parse_number(line, 4, 2)
    if len(splited) <= 1:
        return splited[0] # first play ?
    if len(splited) >= 2:
        splited = splited[0:2]
    if side == 1:
        before, after = splited
    else:
        after, before = splited
    return after

def great_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("GREAT", "").strip()
    return parse_number(line, 4, 1)[0]

def good_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("GOOD", "").strip()
    return parse_number(line, 4, 1)[0]

def bad_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("BAD", "").strip()
    return parse_number(line, 4, 1)[0]

def poor_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("POOR", "").strip()
    return parse_number(line, 4, 1)[0]

def cb_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("COMBO BREAK", "").strip()
    return parse_number(line, 4, 1)[0]

def fast_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("FAST", "").strip()
    return parse_number(line, 4, 1)[0]

def slow_count(line, side=1):
    line = re.sub(r'\s+', " ", line)
    line = line.replace("SLOW", "").strip()
    return parse_number(line, 4, 1)[0]

print("---------------------------------")

doc = {}
i = 1
pgreat_notyet = True
while i < len(descs):
    line = descs[i]
    if line.startswith("CLEAR"):
        doc['lamp'] = clear_lamp(line)
    if line.startswith("DJ"):
        doc['dj_level'] = dj_level(line)
    if line.startswith("EX"):
        doc['ex_score'] = ex_score(line)
    if line.startswith("MISS"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['miss_count'] = miss_count(line)
    if line.startswith("GREAT"):
        if  pgreat_notyet:
            if not any([c.isdigit() for c in line]):
                line += descs[i+1]
                i+=1
            doc['pgreat'] = great_count(line)
            pgreat_notyet = False
        else:
            if not any([c.isdigit() for c in line]):
                line += descs[i+1]
                i+=1
            doc['great'] = great_count(line)
    if line.startswith("GOOD"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['good_count'] = good_count(line)
    if line.startswith("BAD"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['bad_count'] = bad_count(line)
    if line.startswith("POOR"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['poor_count'] = poor_count(line)
    if line.startswith("COMBO"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['cb_count'] = cb_count(line)
    if line.startswith("FAST"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['fast_count'] = fast_count(line)
    if line.startswith("SLOW"):
        if not any([c.isdigit() for c in line]):
            line += descs[i+1]
            i+=1
        doc['slow_count'] = slow_count(line)
        break
    i += 1

doc['track'] = descs[len(descs)-2]

print(doc)

#%%
