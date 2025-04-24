
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice =input("Enter choice")
num1 = input("Enter first number")
num2 = input("Enter second number")

if num1.replace('.','',1).isdigit() and num2.replace('.','',1).isdigit():
        num1 = float(num1)
            num2 = float(num2)
        else:
                print("Invalid input")

                if choice == '1':
                        print(num1 + num2)
                    elif choice == '2':
                            print(num1 - num2)
                        elif choice == '3':
                                print(num1 * num2)
                            elif choice == '4':
                                    if num2 == 0:
                                                print("Cannot divide by zero")
                                                    else:
                                                                print(num1 / num2)
                                                            else:
                                                                    print("Invalid input")

                                                                    
