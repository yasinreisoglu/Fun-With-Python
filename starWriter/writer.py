options = {
    'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
    'B': ['***  ', '*  * ', '**** ', '*  * ', '***  '],
    'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
    'D': ['***  ','*  * ','*  * ','*  * ','***  '],
    'E': ['*****','*    ','*****','*    ','*****'],
    'F': ['*****','*    ','*****','*    ','*    '],
    'G': ['*****','*    ','*  **','*   *','*****'],
    'H': ['*   *','*   *','*****','*   *','*   *'],
    'I': ['  *  ','  *  ','  *  ','  *  ','  *  '],
    'İ': ['  *  ','     ','  *  ','  *  ','  *  '],
    'J': ['*****','    *','    *','*   *',' *** '],
    'K': ['*   *', '*  * ', '***  ', '*  * ', '*   *'],
    'L': ['*    ','*    ','*    ','*    ','*****',],
    'M': ['*   *','** **','* * *','*   *','*   *'],
    'N': ['*   *', '*  **', '* * *', '**  *', '*   *'],
    'O': ['*****', '*   *', '*   *', '*   *', '*****'],
    'P': ['*****','*   *','*****','*    ','*    '],
    'R': ['*****','*   *','**** ','*   *','*   *'],
    'S': ['*****','*    ','*****','    *','*****'],
    'T': ['*****','  *  ','  *  ','  *  ','  *  '],   
    'U': ['*   *','*   *','*   *','*   *','*****'],
    'V': ['*   *','*   *','*   *',' * * ','  *  '],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'Z': ['*****','    *','  *  ',' *   ','*****'],
    ' ': ['     ','     ','     ','     ','     '],
}



def print_big(newList):
    newList = newList.upper()
    for i in range(5):  # length of a list in dictionary is 5
        for j, _ in enumerate(newList):
            print(options[newList[j]][i]+"   ", end=" ")
        print()

word = "HAYAT"
word2 = "GUZEL"
print_big(word)
print_big(word2)