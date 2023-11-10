def wordlen():
    words=[x for x in input("enter the words: ").split()]  #accepts words separated by a space as input 
    lengths=[len(x) for x in words]
    print(max(lengths))
wordlen()
