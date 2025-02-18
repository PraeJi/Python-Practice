# แปลงอุณหภูมิ
# F to C : C=(F-32)*(5/9)
# C to F : F=C*(9/5)+32

temp = input("ป้อนอุณหภูมิ (องศา) : ")

degree = temp[:-1] #อุณหภูมิ
unit = temp[-1].upper() #หน่วย

if unit == "C":
    print("C to F =",int(degree)*(9/5)+32)
elif unit == "F":
    print("F to C =",(int(degree)-32)*(5/9))
