import heapq


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
    james = [sanitize(ts) for ts in james]

with open(r'data/julie.txt') as julief:
    julie = julief.readline().strip().split(',')
    julie = [sanitize(ts) for ts in julie]

with open(r'data/mikey.txt') as mikeyf:
    mikey = mikeyf.readline().strip().split(',')
    mikey = [sanitize(ts) for ts in mikey]

with open(r'data/sarah.txt') as sarahf:
    sarah = sarahf.readline().strip().split(',')
    sarah = [sanitize(ts) for ts in sarah]

print(james)
print(heapq.nsmallest(3, set(james)))
print(julie)
print(heapq.nsmallest(3, set(julie)))
print(mikey)
print(heapq.nsmallest(3, set(mikey)))
print(sarah)
print(heapq.nsmallest(3, set(sarah)))
