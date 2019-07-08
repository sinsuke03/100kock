def g(target):
    target_list = []
    result = ""
    for i in range(0,len(target)):
        if target[i].islower():
            target_list.insert(i,chr(219 - ord(target[i])))
        else:
            target_list.insert(i,target[i])

    for ii in range(0,len(target)):
        result += target_list[ii]

    return result

print(g("Type"))