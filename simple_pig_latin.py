# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    sentence_words = text.split(" ")
    final_list = []
    
    for i in sentence_words:
        first_letter = i[0]
        i = i[1:]
        i=i+first_letter
        i=i+"ay"
        final_list.append(i)

    print(" ".join(final_list))


if __name__ == "__main__":
    pig_it("Hello world !")