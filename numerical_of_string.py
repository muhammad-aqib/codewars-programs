# input   =  "Hello, World!"
# result  =  "1112111121311"

# input   =  "aaaaaaaaaaaa"
# result  =  "123456789101112"


def numericals(s):
    string_final = ""
    list1 = []
    for i in range(len(s)):
        list1.append(s[i])
        count = list1.count(s[i])
        string_final += str(count)
    return string_final


if __name__ == "__main__":
    print(numericals("Hello, World! It's me, JomoPipi!"))
