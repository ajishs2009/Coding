def match_word(words):
    ctr = 0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("The words with first and last characters same: ",lst)
    return ctr
count = match_word(['abc','czc','xyz','1231'])
print("The number of words having first and last words same is:", count)