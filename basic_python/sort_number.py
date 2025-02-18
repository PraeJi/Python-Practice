# รับและเรียงลำดับข้อมูลตัวเลข
# use function "sort"

number = []
while True:
    x = int(input("ป้อนตัวเลข : "))
    if x < 0:
        break
    
    number.append(x)
    
print("Before sort :",number)
number.sort()
print("Sort min to max :",number)
number.reverse()
print ("Sort max to min :",number)
