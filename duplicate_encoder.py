
def duplicate_encode(word):
    final_string = ""
    
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            final_string = final_string + ")"
        else: 
            final_string = final_string + "("

    return final_string


if __name__ == "__main__":
    print(duplicate_encode("(( @"))