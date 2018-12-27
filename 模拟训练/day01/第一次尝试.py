"""


"""

import time

start_time = time.time()

# 三重循环嵌套
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            # print(a, b, c)
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a:%s, b:%s, c:%s" % (a, b, c))

stop_time = time.time()

print("cost：", stop_time - start_time)
"""
a:0, b:500, c:500
a:200, b:375, c:425
a:375, b:200, c:425
a:500, b:0, c:500
cost： 330.43381452560425
"""