def f(a=2, b=3):
    return a + b


print(f(1, 2))
print(f(4))
print(f())
print(f(b=4))
print(f(b=4, a=8))


def g():
    return 4, 5


primeiro, segundo = g()
print(primeiro, segundo)
