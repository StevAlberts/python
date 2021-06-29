# write a program that + - x or /
# separate function to display results


def div(x,y):
    if y!=0:
        return int(x)/int(y)
    else:
        return "Cant divide by 0."

def result (ch, num1, num2):
    
    if ch == 1:
        result = num1 + num2
    elif ch == 2:
        result = num1 - num2
    elif ch == 3:
        result = num1 * num2
    elif ch == 4:
        result = div(num1,num2)
    else:
        print("Input character is not recognized!")

    print('Answer :', result)


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter: \n 1 - add \n 2 - subtract \n 3 - multipy \n 4 - divide \nOption : ")

result(ch, num1, num2)