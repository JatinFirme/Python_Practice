num_1 = int(input("Enter the Value:"))
num_2 = int(input("Enter the Value:"))
choice = input("please select any airthmatic operation + - * /")
if choice == "+":
    sum = num_1 + num_2
    print("The sum for the value is:",sum)
elif choice == "-":
    diff = num_1 - num_2
    print("The diff of the value is:",diff)
elif choice == "*":
    mul = num_1 * num_2
    print("The value of multiplication is:",mul)
elif choice == "/":
    div = num_1 / num_2
    printf("The division for the value is:",div)
else:
    print("invalid choice")
