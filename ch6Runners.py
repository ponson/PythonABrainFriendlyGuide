def sanitize(time_setting):
    if '-' in time_setting:
        splitter = '-'
    elif ':' in time_setting:
        splitter = ':'
    else:
        return time_setting

    (mins, secs) = time_setting.split(splitter)

    return (mins + '.' + secs)

def get_coach_data(filename):
    try: 
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as ioerr:
        print('File error: '+ str(ioerr))
        return None


sarah = get_coach_data(r'data/sarah.txt')
sarah_name, sarah_dob = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))