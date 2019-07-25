# coding: utf-8

i = 0
with open('hightemp.txt',encoding='UTF-8') as datafile:
    for line in datafile:
        print(line.strip("\n"))
        i += 1

print(i)