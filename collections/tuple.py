# tuples 元组

(x, y) = (100, 200)

print(x, y)


scoresDict = {'a': 100, 'b': 50, 'c': 150}
tmp = list()
for k, v in scoresDict.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)

print(tmp)


# 简写
print(sorted([(v, k) for k, v in scoresDict.items( )]))