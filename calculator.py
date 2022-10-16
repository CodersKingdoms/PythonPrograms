import math
def main():
    print("Basic calculator")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division Floating type")
    print("5. Power n")
    print("6. Distance between a point from origin")
    n = int(input("Enter your choice  "))
    if n == 1:
        c = int(input("Enter how many number you have to add  "))
        print("Enter numbers")
        lists = list(())
        for i in range(0,c):
            lists.append(int(input("Enter number  ")))
        print("Sum is : ",math.fsum(lists))
    if n == 2:
        c = int(input("Enter 1st number  "))
        d = int(input("Enter 2nd number  "))
        print("Difference is : ", c-d)
    if n == 3:
        c = int(input("Enter how many number you have to multiply  "))
        print("Enter numbers")
        lists = list(())
        for i in range(0,c):
            lists.append(int(input("Enter number  ")))
        print("Product is : ",math.prod(lists))
    if n == 4:
        c = int(input("Enter 1st number  "))
        d = int(input("Enter 2nd number  "))
        print("Division is : ", c/d)
    if n == 5:
        c = int(input("Enter number a  "))
        d = int(input("Enter power n  "))
        print("a^n is : ", c**d)
    if n == 6:
        c = int(input("Enter 1st coordinate of point  "))
        d = int(input("Enter 2nd coordinate of point  "))
        l = list((c,d))
        o = list((0,0))
        print("Distance from origin is : ", math.dist(l,o))

if __name__ == '__main__':
    main()
