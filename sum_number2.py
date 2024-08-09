start,stop = 1,5
sum = 0

while start<=stop:
    num = int(input("ป้อนตัวเลขของคุณ : "))
    sum+=num
    start+=1
    
print("ผลรวมเท่ากับ",sum)
print("ค่าเฉลี่ยเท่ากับ",sum/stop)