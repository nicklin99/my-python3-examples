# 找出list中是否存在重复名称

apis = ["test", "upload", "delete", "upload", "last"]
counts = dict()

for name in apis:
    counts[name] = counts.get(name, 0) + 1

print(counts)


firstRepeatName = None
firstRepeatCount = 0

print("keys():", counts.keys())
print("values():", counts.values())

for key, count in counts.items():
    print(key, count)
    if firstRepeatName is None and count > 1:
        firstRepeatName = key
        firstRepeatCount = count

print("重复的名称:", firstRepeatName)
print("重复的次数:", firstRepeatCount - 1)
