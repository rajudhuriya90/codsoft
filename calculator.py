print("**********SIMPLE CALCULATOR ****************")

num1=float(input("Enter First Number here:"))
num2=float(input("Enter Second Number here:"))

print("Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division")

choice=int(input("Enter your choice from 1-4:"))
if choice==1:
    sum=num1+num2
    print(" The Addition of given Number is =",sum)
elif choice==2:
    sub=num1-num2
    print(" The Subtraction of given Number is=",sub)
elif choice==3:
    mult=num1*num2
    print(" The Multiplication of given Number is =",mult) 
elif choice==4:
    div=num1/num2
    print(" The Division of given number is =",div) 
else:
    print("Invalid choice !!!!! please Enter correct choice !")              