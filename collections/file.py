

import json
import time


print(dir())

# 读
with open("collections/versions.txt", "r") as freader:
    data = freader.read()
    print(data)

print(freader.closed)

# 完全写入
with open("collections/versions.txt", "w") as fwriter:
    fwriter.write("1.3\n")

print(fwriter.closed)


# 追加写入
with open("collections/versions.txt", "a") as fappend:
    fappend.write("1.4\n")


# 读取每行


