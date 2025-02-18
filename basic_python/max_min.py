# หาตัวเลขมากสุด/น้อยสุด

max,min = 0,999999

while True:
    num = int(input("ป้อนตัวเลขของคุณ: "))
    if num<0:
        break
    elif num>=max:
        max = num
    elif num<=min:
        min = num
        
print("ตัวเลขมากที่สุดคือ",max)
print("ตัวเลขที่น้อยที่สุดคือ",min)
