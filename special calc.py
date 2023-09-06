num1= float(input("enter the number"))
num2= float(input("eneter the second nummber"))
operator= input("opeartion you used to perform")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("operation is failed")

