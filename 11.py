# coding: utf-8

with open('hightemp.txt',encoding='UTF-8') as datafile:
    for line in datafile:
        print(line.replace("\t"," ").strip("\n"))
