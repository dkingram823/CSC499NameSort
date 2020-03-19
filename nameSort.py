if __name__== "__main__":
    file1 = open("Sort Me.txt","r")

    strForm = file1.read()
    wordlist = []

    next = False
    thisWord = ""
    for n in range(strForm.__len__()):
        if not next and strForm[n] != '\n':
            thisWord += strForm[n]
        elif not next and strForm[n] == '\n':
            next = True
            wordlist.append(thisWord)
            thisWord = ""
        else:
            next = False
            # take no action, skip 'n'

    print('')
    print(wordlist)
