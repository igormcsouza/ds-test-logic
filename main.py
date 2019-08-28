# Grouping mensages by users

import json
from datetime import datetime

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
            min = float(ts)/1000
            max = float(idx['ts'])/1000
            delta = (datetime.utcfromtimestamp(max) - datetime.utcfromtimestamp(min)).total_seconds() / 60
            print(delta)
            if delta < 2:
                found = True
                break

        if found:
            result[idx['user']][ts].append(idx)
        else:
            result[idx['user']][idx['ts']] = list()
            result[idx['user']][idx['ts']].append(idx)
    else:
        result[idx['user']] = dict()
        result[idx['user']][idx['ts']] = list()
        result[idx['user']][idx['ts']].append(idx)

print(result['U1ZQR43RB'].keys())
print('\n... Done!')

print('\nWriting File!...')
for user in result:
    with open('data/' + user + '.json', 'w') as f:
        json.dump(result[user], f)
print('...Complete!!')