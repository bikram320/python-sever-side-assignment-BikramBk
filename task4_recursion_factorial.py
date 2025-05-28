#program to find the factorial of entered number using recursion

def fact(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n*fact(n-1)

def main():
    number = int (input("Enter a number : "))
    if number<0:
        print("Enter a Valid number :")

    else :
        result = fact(number)
        print(f"Factorial of number : {result}")

#Calling main Function
main()