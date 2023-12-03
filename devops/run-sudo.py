from invoke.watchers import Responder


resolvePassword = Responder(
    pattern=r'\[sudo\] password:',
    response='mypassword\n',
)


def sudo(c):
    try:
        result = c.run("uname -a")
        c.sudo("whoami")
        print(result)
    except:
        print("failed")
