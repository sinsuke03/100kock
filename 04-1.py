'''
m ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
m = m.replace(',',"").replace('.',"").split(" ")
print(m)
y = []
y.append(m)
print(y)
for i in range(len(y)):
    print(i)
    '''

line = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
line = line.replace(',', "").replace('.', "").split(" ")
# y = []
# for i in line:
#    print(i)
#   #  print(len(i))
#
# print(line[2])
z = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for m,q in enumerate(line,1):
    # if m == 19:
    #     print(q)
    # elif m == 0:
    #     print(q[::])
    if m <= 20:
        # print(m,q[:2])
        if m in z:
            print(m,q[:1])
        else:
            print(m,q[:2])