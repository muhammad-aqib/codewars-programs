

def main(inputString):
    print(inputString)
    final_list = []
    for i in range(len(inputString)):
        final_list.append("0")

    for i in inputString:
        if not i.isalpha():
            index = inputString.index(i)
            inputString = inputString.replace(i,"-",1)
            final_list[index]=i
    
    for i in inputString:
        if i.isalpha():
            index = inputString.index(i)
            inputString = inputString.replace(i,"-",1)
            final_index = -(index + 1)
            final_list[final_index]=i
    print("".join(final_list))    


if __name__ == "__main__":
    main("sami$bh$a")