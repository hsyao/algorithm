"""


"""

lis = [23, 45, 5, 8, 50, 78, 54, 87]

# 设置冒泡排序执行标志
# sort_flag = False

# count = 0
# step = len(lis)
# for i in range(1, step-1):
#     for j in range(0, step - i):
#         if lis[j] > lis[j + 1]:
#             temp = lis[j]
#             lis[j] = lis[j + 1]
#             lis[j + 1] = temp
#         count += 1
#
# print(lis)
# print(count)


# lis.sort()
# print(lis)

# 插入排序实现算法


# 初始设定列表第一个元素属于已排序区间，剩余元素属于未排序区间
# 遍历为排序区间元素，与已排序区间元素比较大小，确定插入位置
# step = len(lis)
# print(step)
# for i in range(1, step):
#     temp = lis[i]
#
#     # 比较已排序区间元素，找到插入位置
#     for j in range(0, i-1):
#         # 若待排序元素小于已排序元素的值，先移动元素
#         if temp < lis[j]:
#             m = i  # 获取待排序位置下标，后续提供移动位置递减使用
#             for k in range(j, i):  # 从开始移动的位置到待排序的前一个元素位置作为区间下标
#                 lis[m] = lis[m-1]
#                 m -= 1
#             lis[j] = temp
#             break

# print(lis)

# step = len(lis)
# print(step)
#
# for i in range(1, step):
#
#     temp = lis[i]
#     j = i
#     for k in range(0, i):
#
#         if lis[j-1] > temp:  # 移动元素
#             lis[j] = lis[j-1]
#             j -= 1
#         else:
#             break
#     lis[j] = temp
#
# print(lis)


# 选择排序算法实现
step = len(lis)
print(step)


for i in range(0, step-1):

    # 遍历未排序区间做最小值的选择后交换
    for j in range(i+1, step):
        if lis[j] < lis[i]:  # 做最小值交换处理
            temp = lis[j]
            lis[j] = lis[i]
            lis[i] = temp


print(lis)
