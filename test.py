"""斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。"""

value = list()


def fo(num):
    """计算斐波，前两个数相加"""
    n1 = 0
    n2 = 1
    k = 2
    if num == 0:
        value.clear()
    elif num == 1:
        value.append(n1)
    else:
        value.append(n1)
        value.append(n2)
    # 输入了一个4
    while k <= num:
        new = n1 + n2
        value.append(new)
        n1 = n2
        n2 = new
        k += 1
    print(value)
    value.clear()


while True:
    i = input("打印几项，只能填正整数？不想玩请按q > ")
    if i.isnumeric():
        fo(int(i))
    elif i == 'q':
        break
    else:
        print("请正确输入")
        i = None
