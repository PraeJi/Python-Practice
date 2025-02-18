# ตารางหมากฮอต
'''
3x3
oxo
xox
oxo
'''

num = int(input("ป้อนตัวเลข : "))
for row in range(num):
    for column in range(num):
        if row%2 == 0:
            if column%2 == 0:
                print("o",end="")
            else:
                print("x",end="")
        else:
            if column%2 == 0:
                print("x",end="")
            else:
                print("o",end="")
    print("")
