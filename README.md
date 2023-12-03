# my-python3-examples

个人python3 学习与练习代码目录说明

`collections` 学习、练习基本语法

`devops` 运维脚本,使用 fabric包

## collections 学习集合

- var.py 变量声明
- list.py 集合： list dict
- tuple.py 集合操作
- func.py 函数
- file.py version.py 文件读写
- img img包

## devops 运维

fabric 配置文件在 `~/.fabric.yaml`

```yaml
connect_kwargs: 
    password: 
miniblog:
  image: 
```

.ssh/config

```bash
Host A
    HostName hosta
    User root
    PasswordAuthentication Yes

Host B
    HostName hostb
    User root
    IdentityFile ~/.ssh/your.pem
```

```bash
fab --list

# 在host A 远程执行 task version
fab -H A version

# 查看帮助, -h 一定要放在名称前
fab -h miniblog 
```