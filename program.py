import math

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(s):
    start = 1
    final = []
    for i in range(len(s)):
        new_list = []
        alpha = s[i]
        for j in range(i + 1):
            if j == 0:
                new_list.append(alpha.upper())
            else:
                new_list.append(alpha.lower())
        final.append(new_list)
    my_list = []
    for i in final:
        my_list.append("".join(i))
    my_list = "-".join(my_list)
    return my_list


def main():
    print(accum("ajshdljahsdkjashdkjas"))


if __name__ == "__main__":
    main()
