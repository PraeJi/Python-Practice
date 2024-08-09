# ตัวเลขขั้นบันได
'''
input = 5
1
12
123
1234
12345
'''

last = int(input("ป้อนตัวเลข : "))

for row in range(1,last+1):
    for column in range(1,row+1):
        print(column,end='')
    print(" ")