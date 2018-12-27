"""


"""

from timeit import Timer

x = list(range(2000000))

pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero", pop_zero.timeit(1000), "seconds")

x = list(range(2000000))

pop_end = Timer("x.pop()", "from __main__ import x")
print("pop_end", pop_end.timeit(number=1000), "seconds")

"""
pop_zero 4.080373721443814 seconds
pop_end 0.00019547532370012277 seconds
"""

x = list(range(2000000))

append = Timer("x.append(1)", "from __main__ import x")
print("append", append.timeit(1000), "seconds")

x = list(range(2000000))

insert = Timer("x.insert(0,1)", "from __main__ import x")
print("insert", insert.timeit(1000), "seconds")


"""
append 0.00014158059550251068 seconds
insert 4.694208155983319 seconds
"""