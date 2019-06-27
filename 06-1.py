def n_gram(d,n):
    list = []
    for i in range(len(d) - n + 1):
        list.append(d[i: n + i])
    return list

x = "paraparaparadise"
y = "paragraph"

xlist = n_gram(x,2)

ylist = n_gram(y,2)


# setw = set(xlist + ylist)

setx = set(xlist)
print(setx)
sety = set(ylist)
print(sety)
print(setx | sety)
print(setx & sety)
print(setx - sety)
print(sety - setx)

print("se" in xlist)
print("se" in ylist)
