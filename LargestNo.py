def main():

    n1 = int(input("Enter the 1st no."))
    n2 = int(input("Enter the 1st no."))
    n3 = int(input("Enter the 1st no."))
    n4 = int(input("Enter the 1st no."))

    s = eval(input("Enter expression"))
    print(s)

    sum = n1 + n2 + n3 + n4
    for i in range(sum):
        if i == n1 or i == n2 or i == n3 or i == n4:
            Large  = i
    print("Largest number is : ",Large)
    print("End of program")

if __name__ == '__main__':
    main()
