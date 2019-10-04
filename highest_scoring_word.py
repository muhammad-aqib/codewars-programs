# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    word_list = x.split(" ")
    word_dict={}

    for i in word_list:
        word_dict[i]=0
    
    for word in word_list:
        asci_code_sum=0
        for j in range(len(word)):
            asci_code_sum =  asci_code_sum + ord(word[j])
        word_dict[word] = asci_code_sum
    
    value_list=[]
    for k,v in word_dict.items():
        value_list.append(v)
    
    max_val=max(value_list)
    print(max_val)

    for k,v in word_dict.items():
        if v == max_val:
            ans = k

    return ans


if __name__ == "__main__":
    print(high("man i need a taxi up to ubud"))