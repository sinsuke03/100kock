m = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
m = m.replace(',',"").replace('.',"").split(" ")
y = []
print(m)
for i in m:
    print(len(i))
    y.append(len(i))
print(y)
'''
input関数	標準入力から1行読み込む
line = input()

rstrip関数	文字列の末尾の改行コードを取り除きます。

line = input().rstrip()

split関数	与えられたデータを指定の記号で分割し、リストとして戻す

line = "勇者,戦士,魔法使い"
p line.split(",")

'''