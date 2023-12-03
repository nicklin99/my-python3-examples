

def say(word):
    '''say function'''
    print(word)


say('hello')


# 关键词参数
# title 必须参数
# keyword 可选参数
def prompt(title, keyword=""):
    print("title:", title)
    print("keyword:", keyword)


prompt("123,abc", "keyword")
prompt('title', keyword="123,abc")


def ask_ok(title):
    print("ask :", title)


ask_ok("how old are you?")
ask_ok(title="how old are you?")

# / 位置参数
# 限制必须是位置参数


def ask(title, /):
    print("ask :", title)


ask("where are your from?")

# *关键词参数


def reply(*kwds):
    print("keywords param", kwds)


reply({'name': 'name'})

# 可变参数


def concat(*args, sep=","):
    return sep.join(args)


print(concat("a", "b", "c"))
print(concat("a", "b", "c", sep=">"))


# 可变关键词参数

def rangeDic(**args):
    for key in args:
        print(key, args[key])


rangeDic(fullname={'first': 'nick', 'last': 'lin'})


# 打印函数doc

def sayNothing():
    '''say nothing'''
    pass


print(sayNothing.__doc__)

# 函数注解


def sayBye(word) -> str:
    print(sayBye.__annotations__)
    return word


print(sayBye("bye bye"))

# 匿名函数


def sub(n):
    return lambda x: x-n


f = sub(10)

print(f(100))
