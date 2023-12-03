import sys
from fabric import task, Connection


@task
def version(c: Connection):
    """
    版本号
    """
    print(c)
    print('1.0')
    c.run("whoami")
    print(c.config.miniblog.image)


@task(help={'app': 'app包名称', 'target': '远程主机路径'})
def scptar(c, app: str, target: str):
    '''
    上传应用文件后解压到target目录
    查看帮助 fab -h scptar
    '''

    try:
        if c.run('test -d ' + target, warn=True).failed:
            c.run("mkdir " + target)

        result = c.put(app, remote=target)
        print("Uploaded {0.local} to {0.remote}".format(result))
        c.run("tar -C {} -xzvf {}".format(target, app))
    except:
        info = sys.exc_info()
        print("failed:", info[1], info[0])


@task
def miniblog(c):
    '''
    部署mini作品展示页
    '''
    if c.config.miniblog.image is None:
        print("镜像不能为空，请在~/..fabric.yaml中配置miniblog.image")
        raise

    try:
        c.run("docker pull {}".format(c.config.miniblog.image))
        c.run("docker rm -f miniblog")
        c.run(
            "docker run --name miniblog -dp 8092:8092 --privileged --network docker_frontend " + c.config.miniblog.image)
    except:
        info = sys.exc_info()
        print("failed:", info[1], info[0])
