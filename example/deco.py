def g(func):
    def wrapper():
        print('g1')
        func()
        print('g2')
    return wrapper


def h(func):
    def wrapper():
        print('h1')
        func()
        print('h2')
    return wrapper

# @h
# @g


def f():
    print('hello')


f = h(g(f))

f()
