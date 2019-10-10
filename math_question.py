# ABC = A! + B! +C!
# find A, B, C

# A, B, C are all single digits (edited) 
# ABC is a 3 digit number

import math

def main():
    for i in range(100,1000):
        sumNums = 0
        string_number = str(i)
        for j in string_number:
            number = int(j)
            number = math.factorial(number)
            sumNums = sumNums + number
            
            if sumNums == i:
                print(sumNums)
        

if __name__ == "__main__":
    main()