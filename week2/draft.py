def func3(index):
    # 規律是 減2[1], 減3[2], 加1[3], 加2[4]
    # 先不考慮index == 0
    q = index//4
    r = index%4
    # index +1 第幾個數字 index = 6; 6//4 = 1; 6%4 = 2; 25-2*q+ -5
    if r == 1:
        r_num = -2
    elif r == 2:
        r_num = -5
    elif r == 3:
        r_num = -4
    elif r == 0:
        r_num = -2
    val = 25-2*q+r_num

    return print(val)
