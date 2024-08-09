# สร้างภาพวาดสี่เหลี่ยมจัตุรัส

'''
3x3
xxx
xxx
xxx
'''

num =  int(input("ป้อนตัวเลข : "))

for row in range(num):
    for column in range(num):
        print("x",end="")
        
    print(" ")
    
'''
x
xx
xxx
'''

for i in range(num+1):
    for j in range(i):
        print("x",end="")
    print("")