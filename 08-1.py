def g(target):
    result = ""
    target_list = []
    for i in range(0,len(target)):
        if target[i].islower():
            target_list.insert(i,chr(219 - ord(target[i])))
        else:
            target_list.insert(i,target[i])

    for ii in range(0,len(target)):
        result += target_list[ii]

    return result

target = "Type"
e = g(target)
f = g(e)
print(e)
print(f)