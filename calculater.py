while True:
    print("***** enter your option******")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.quit calculator")

    choice=int(input("enter your option"))
    try:
        if choice==1:
            n1=int(input("enter your first number"))
            n2=int(input("enter your second"))
            print(n1+n2)
        elif choice==2:
            n1=int(input("enter your first number"))
            n2=int(input("enter your second"))
            print(n1-n2)
        elif choice==3:
            n1=int(input("enter your first number"))
            n2=int(input("enter your second"))
            print(n1*n2)
        elif choice==4:
            n1=int(input("enter your first number"))
            n2=int(input("enter your second"))
            if n2==0:
                print("cannot divide by zero")
            else:
                print(n1/n2)
        elif choice==5:
            break
    except ValueError:
        print("invalid input please enter valid inputs")
    print("Thank you for using calculator")



