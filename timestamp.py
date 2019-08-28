import datetime

min = 1471110886.000004/1000           #removing milli seconds
max = 1471194112.000016/1000

min = datetime.datetime.fromtimestamp(min)
max = datetime.datetime.fromtimestamp(max)

print("Total Minutes : " + str((max-min).total_seconds() / 60))