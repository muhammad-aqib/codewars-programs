# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    strNum = str(num)
    output = ""
    for i in range(len(strNum)):
        temp = int(strNum[i])
        final_num = temp*temp
        output = output + str(final_num)
    return int(output)


if __name__ == "__main__":
    print(square_digits(9119))
