# coding: utf-8
import random

def Typoglycemia(target):
    x_list = []
    for word in target.split(" "):
        if len(word) <= 4:
            x_list.append(word)
        else:
            temp_list = list(word[1:-1])
            random.shuffle(temp_list)
            x_list.append(word[0] + "".join(temp_list) + word[-1])

    return x_list

x ="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = Typoglycemia(x)
print(s)