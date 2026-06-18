# task1------------

def func1(name):
    points = {"⾟巴":(-3,3), "悟空":(0,0), "弗利沙":(4,-1), "特南克斯":(1,-2), "丁滿":(-1,4), "貝吉塔":(-4,-1)}
    # 查了一下數學上怎麼判斷點在線的哪一邊
    # y = -1.2x + 1.8 
    # (0,1.8)/ (1.5,0)
    # 1.2x + y - 1.8 ><= 0
    target0 = points[name]
    side_num_target0 = 1.2* target0[0] +target0[1]-1.8
    dis_list = []
    side_list = []
    name_list = ["⾟巴", "悟空", "弗利沙", "特南克斯", "丁滿", "貝吉塔"]
    total_list = []
    for p in points:
        target = points[p]
        side_num_target = 1.2* target[0] +target[1]-1.8
        if side_num_target0 > 0 and side_num_target< 0: # 邊界條件:沒有剛好是12或18的座標，所以不會有0
            side = 2
        elif side_num_target0 < 0 and side_num_target> 0:
            side = 2
        else:
            side = 0
        side_list.append(side)
        dis_x = target[0] - target0[0] # tuple不能相減/ points[p] 取得key 而不value
        dis_y = target[1] - target0[1]
        dis = abs(dis_x) + abs(dis_y)
        dis_list.append(dis)
    # return dis_list, side_list   # list to do: max逐一比較而不是列出整個list，可能比較有效率
    # 先相加 再找名字
    for n in range(len(name_list)): # 邊界條件:0是自己
        total = dis_list[n] +side_list[n]
        total_list.append(total)

    for n in range(len(name_list)):
        if total_list[n] == 0:
            total_list.pop(n) # 不會有兩個0; 修改的原始序列不是好行為
            name_list.pop(n)
            break # 不然會報錯: list index out of range

    furthest = max(total_list)
    nearest = min(total_list)

    furthest_name = []
    nearest_name = []
    
    for n in range(len(name_list)):
        if total_list[n] == furthest:
            furthest_name.append(name_list[n]) # 有兩個怎麼辦 -> list 解決
        if total_list[n] == nearest:
            nearest_name.append(name_list[n])

    # return furthest, nearest, furthest_name, nearest_name #試著用OOP寫?
    return print(f"最遠{", ".join(furthest_name)}；最近{"、".join(nearest_name)}")
# 最遠dis_list.max()；最近dis_list.min() # 要人名不是數值  # points[p]
# print(func1("⾟巴"))

func1("⾟巴") # print 最遠弗利沙；最近丁滿、⾙吉塔
func1("悟空") # print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙") # print 最遠⾟巴，最近特南克斯
func1("特南克斯") # print 最遠丁滿，最近悟空

# task2------------
'''
# your code here, maybe
def func2(ss, start, end, criteria):
# your code here
services=[
{"name":"S1", "r":4.5, "c":1000},
{"name":"S2", "r":3, "c":1200},
{"name":"S3", "r":3.8, "c":800}
] 
func2(services, 15, 17, "c>=800") # S3
func2(services, 11, 13, "r<=4") # S3
func2(services, 10, 12, "name=S3") # Sorry
func2(services, 15, 18, "r>=4.5") # S1
func2(services, 16, 18, "r>=4") # Sorry
func2(services, 13, 17, "name=S1") # Sorry
func2(services, 8, 9, "c<=1500") # S2

# task3------------

def func3(index):
# your code here
func3(1) # print 23
func3(5) # print 21
func3(10) # print 16
func3(30) # print 6

# task4------------
def func4(sp, stat, n):
# your code here
func4([3, 1, 5, 4, 3, 2], "101000", 2) # print 5
func4([1, 0, 5, 1, 3], "10100", 4) # print 4
func4([4, 6, 5, 8], "1000", 4) # print 2
"""