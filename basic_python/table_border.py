# สร้างขอบตาราง

'''
4x4
  0123
0 xxxx
1 x  x
2 x  x
3 xxxx
'''

num = int(input("ป้อนตัวเลข : "))
for row in range(num):
    if row==0 or row==num-1:
        for column in range(num):
            print("x",end="")
        print("")
    else:
        for column in range(num):
            if column==0 or column==num-1:
                print("x",end="")
            else:
                print(end=" ")
        print("")
    
