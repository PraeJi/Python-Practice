# Summation ex. 1+2+3...

start = int(input("Start = ")) #start number
step = int(input("Step = ")) #step number
end = int(input("End = ")) #end number
summation = 0 #เก็บผลรวม
count = 0

while start<=end:
    count+=1
    summation+=start
    print("รอบที่",count,"ค่า sum =",summation)
    start+=step
    
print("Summation =", summation)
print("Average =",summation/count)