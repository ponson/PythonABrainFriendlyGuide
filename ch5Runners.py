def sanitize(time_setting):
    if '-' in time_setting:
        splitter = '-'
    elif ':' in time_setting:
        splitter = ':'
    else:
        return time_setting

    (mins, secs) = time_setting.split(splitter)

    return (mins + '.' + secs)



with open(r'data/james.txt') as jamesf:
    james = jamesf.readline().strip().split(',')
    james = sorted(list(set([sanitize(ts) for ts in james])))

with open(r'data/julie.txt') as julief:
    julie = julief.readline().strip().split(',')
    julie = sorted(list(set([sanitize(ts) for ts in julie])))

with open(r'data/mikey.txt') as mikeyf:
    mikey = mikeyf.readline().strip().split(',')
    mikey = sorted(list(set([sanitize(ts) for ts in mikey])))

with open(r'data/sarah.txt') as sarahf:
    sarah = sarahf.readline().strip().split(',')
    sarah = sorted(list(set([sanitize(ts) for ts in sarah])))

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])