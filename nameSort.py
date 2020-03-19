# Daniel Ingram
# 3/18/2020
# CSC 499

def lensort(x):
    for i in range(1, len(x)):
        ind = x[i]
        j = i - 1
        while j >= 0 and ind.__len__() < x[j].__len__():
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = ind
    return x

def alphSort(l,r,x):
    for i in range(l+1,r):
        ind = x[i]
        j = i - 1
        while j >= 0 and ind[0] < x[j][0]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = ind
    return x


if __name__== "__main__":
    file1 = open("Sort Me.txt","r")

    strForm = file1.read()
    wordlist = []

    next = False
    thisWord = ""
    for n in range(strForm.__len__()): # converts the text file to a list
        if not next and strForm[n] != '\n':
            thisWord += strForm[n]
        elif not next and strForm[n] == '\n':
            next = True
            wordlist.append(thisWord)
            thisWord = ""
        else:
            next = False
            # take no action, skip 'n'

    wordlist = lensort(wordlist)

    lastLen = 0
    lastInd = 0
    for n in range(len(wordlist)):
        if wordlist[n].__len__() > lastLen:
            alphSort(lastInd,n,wordlist)
            lastInd = n
            lastLen = wordlist[n].__len__()

    print('')

    for n in wordlist:
        print(n)
