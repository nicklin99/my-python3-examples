import sys


def new_version(c):
    try:
        result = c.put("devops/versions.txt", remote="/opt/")
        print("Uploaded {0.local} to {0.remote}".format(result))
    except:
        info = sys.exc_info()
        print(info[1], info[0])
