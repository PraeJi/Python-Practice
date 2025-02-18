# แม่สูตรคูณ

start = int(input("ป้อนแม่สูตรคูณตัวเริ่มต้น : ")) #แม่สูตรคูณตัวแรก
end = int(input("ป้อนแม่สูตรคูณตัวสุดท้าย : "))

for x in range(start,end+1):
    print("แม่",x)
    for y in range(1,13):
        print(x,"x",y,"=",x*y)
