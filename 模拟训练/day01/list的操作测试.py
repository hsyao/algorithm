"""


"""


def t1():
    l = []
    for i in range(10000):
        l += [i]


def t2():
    l = []
    for i in range(10000):
        l.append(i)


def t3():
    l = [i for i in range(10000)]


def t4():
    l = list(range(10000))


from timeit import Timer

timer1 = Timer("t1()", "from __main__ import t1")
print("contat", timer1.timeit(1000), 'seconds')

timer2 = Timer("t2()", "from __main__ import t2")
print("append", timer2.timeit(1000), 'seconds')

timer3 = Timer("t3()", "from __main__ import t3")
print("comprehension", timer3.timeit(1000), 'seconds')

timer4 = Timer("t4()", "from __main__ import t4")
print("list range", timer4.timeit(1000), 'seconds')
"""
contat 1.8379864587356725 seconds
append 1.779411871639867 seconds
comprehension 0.8569296002251598 seconds
list range 0.4745302496994084 seconds

"""