# Grouping mensages by users

import json, datetime

print('Reading Json File...\n')
with open('U1ZQR43RB.json') as json_file:
    U1ZQR43RB = json.load(json_file)
print(U1ZQR43RB[0].keys())

print('\nCreating a result dictionary...\n')
result = dict()

for idx in U1ZQR43RB:
    if idx['user'] in result.keys():
        found = False
        for ts in result[idx['user']].keys():
            min = datetime.datetime.fromtimestamp(float(ts)/1000)
            max = datetime.datetime.fromtimestamp(float(idx['ts'])/1000)
            delta = (max-min).total_seconds() / 60
            if delta < 2:
                found = True
                break

        if found:
            result[idx['user']][ts].append(idx)
        else:
            result[idx['user']][idx['ts']] = list()
            result[idx['user']][idx['ts']].append(idx)
    else:
        print('Not yet')
        result[idx['user']] = dict()
        result[idx['user']][idx['ts']] = list()
        result[idx['user']][idx['ts']].append(idx)

print(result['USLACKBOT'])

for user in result:
    with open('data/' + user + '.json', 'w') as f:
        json.dump(result[user], f)