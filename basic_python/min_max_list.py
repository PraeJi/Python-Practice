# find number min and max

number_list = []
while True:
    x = int(input("Input number : "))
    if x < 0:
        break
    
    number_list.append(x)
    
print(number_list)
print("Min is:",min(number_list))
print("Max is:",max(number_list))
print("Summation is:",sum(number_list))
