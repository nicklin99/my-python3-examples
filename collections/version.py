import json
import sys
import time


def newVersion(version: str):
    # 写入当前版本号
    with open("collections/version.txt", "w") as fv:
        fv.write(version)

    # 历史版本
    with open("collections/versions.txt", "r") as fr:
        lines = fr.readlines()
        lastVersion = json.loads(lines[len(lines) - 1].replace("\n", ""))
        print("lastVersion", lastVersion)

    with open("collections/versions.txt", "a") as fjsonwriter:
        try:
            line = {'version': version, 'created':  time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime()), 'rollback': lastVersion['version']}
            fjsonwriter.write(json.dumps(line)+"\n")
        except:
            print("err:", sys.exc_info()[1])


newVersion("1.5")
