# Group Even/Odd

even = []
odd = []
while True:
    x = int(input("Input number : "))
    
    if x < 0:
        break
    
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
        
print(odd)
print(even)