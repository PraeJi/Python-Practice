sum = 0

while True:
    num = int(input("ป้อนตัวเลขของคุณ : "))
    sum+=num
    if sum>=100:
        break
    else:
        print("ผลรวม =",sum)
        
print("ผลรวมสุดท้ายเท่ากับ",sum)
