# เกมทายลูกเต๋า

import random

myRandom = random.randrange(1,7)
print("คุณมีโอกาสทั้งหมด 3 ครั้ง")
k=1

while True:
    guess = int(input("ป้อนคำตอบของคุณ : "))
    if guess <= 0 or guess >6 or k==3:
        print("เสียใจด้วย")
        print("เฉลย",myRandom)
        break
    
    if guess < myRandom:
        print("มากกว่า")
    elif guess > myRandom:
        print("น้อยกว่า")
    else:
        print(myRandom,"ถูกต้อง ยินดีด้วย")
        break
    k+=1
