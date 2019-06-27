def n_gram(target,n):
    list = []
    for i in range(len(target) - n + 1):
        list.append(target[i: n + i])

    return list #　計算結果を戻す、戻り値
# この下で定義したものを上に戻す
target = "I am an NLPer"
list = n_gram(target,2) # 関数呼び出しの引数　この場合２つ
print(list)

w_target = target.split(" ")

list = n_gram(w_target,2)
print(list)