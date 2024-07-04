op=input("enter the operator ( + - * / ) : ")
num1=float(input("enter the first number : "))
num2=float(input("enter the second number : "))
if op=="+":
    result=num1+num2
    print(f"the result is {round(result,2)}")
elif op=="-":
    result1=num1-num2
    print(f"the result is {round(result1,2)}")
elif op=="*":
    result2=num1*num2
    print(f"the result is {round(result2,2)}")
else:
    result3=num1/num2
    print(f"the result is {round(result3,2)}")