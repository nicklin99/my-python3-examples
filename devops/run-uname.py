
def uname(c):
    try:
        result = c.run("uname -a")
        c.run("whoami")
        print(result)
    except:
        print("failed")
