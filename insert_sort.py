# _*_ coding=utf-8 _*_


# 插入排序，时间复杂度O(n²)
def insert_sort(arr):
    """
    插入排序；以朴克牌为例，从小到大排序。摸到的牌current与手里的每张牌进行对比，
    手里的牌大于current，则手里的牌往后移；手里的最后一张牌小于current，current最大，结束循环。
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):  # 摸到的牌的index
        # 摸到的牌
        current = arr[i]
        # 手里最后一张牌的index
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            # 继续和前一张牌进行比较
            pre_index -= 1
        # 手里的最后一张牌小于current，current最大
        arr[pre_index + 1] = current
    return arr


num = [4, 5, 3, 7, 6, 9, 8, 10]
print(insert_sort(num))
