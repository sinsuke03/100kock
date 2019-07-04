file = 'hightemp.txt'
count = 0
with open(f) as datafile:
    for line in datafile:
        count += 1
print(count)