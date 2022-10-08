def palindrome(word):
    string_word=str(word)
    reverse_word=string_word[::-1]
    if reverse_word==string_word:
        return True
    # print(reverse_word, word)
    return False

def palindrome_sentences(sentence):
    string_word=str(sentence).lower()

    filtered_word=[]
    for x in string_word:
        if ord(x)>96 and ord(x)<123:
            filtered_word.append(x)

    string_word= "".join(filtered_word)
    print(filtered_word,string_word)
                

    reverse_word=string_word[::-1]
    if reverse_word==string_word:
        return True
    print(reverse_word, string_word)
    return False
print(palindrome_sentences(123))