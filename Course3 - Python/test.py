def sum_two_nums(num1, num2):
    if type(num1) != int or type(num2) != int:
        print("Both inputs should be numbers!")
        return
    return num1 + num2

def sum_even_of_list(list):
    sum = 0
    for num in list:
        if num % 2 == 0:
            sum += num
    return sum

def main():
    print()
    
    input1 = input("Please enter the FIRST number to compute the sum of two numbers: ")
    input2 = input("Please enter the SECOND number to compute the sum of two numbers: ")
    print("The result is " + str(sum_two_nums(int(input1), int(input2))) + ".")

    # list = [1,2,3,4,5,4]
    # print("The sum of even numbers in the list is: " + str(sum_even_of_list(list)))

if __name__ == "__main__":
    main()
