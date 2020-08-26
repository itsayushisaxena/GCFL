print("**********MENU**********")
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter your choice")
x = int(input())
if(x == 1):
    print("Please enter two values to add")
    y1 = int(input())
    y2 = int(input())
    print("Thanks for using it! Your sum is",y1+y2)
elif(x == 2):
    print("Please enter two values to subtraction")
    y1 = int(input())
    y2 = int(input())
    print(y1-y2)
else:
    print("Invalid choice")    
