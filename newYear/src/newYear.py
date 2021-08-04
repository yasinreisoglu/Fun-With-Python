import datetime
from playsound import playsound


options = {
    'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
    'B': ['***  ', '*  * ', '**** ', '*  * ', '***  '],
    'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
    'K': ['*   *', '*  * ', '***  ', '*  * ', '*   *'],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'N': ['*   *', '*  **', '* * *', '**  *', '*   *'],
    'O': ['*****', '*   *', '*   *', '*   *', '*****'],
    'L': ['*    ','*    ','*    ','*    ','*****',],
    'U': ['*   *','*   *','*   *','*   *','*****'],
    ' ': ['     ','     ','     ','     ','     '],
    'R': ['*****','*   *','**** ','*   *','*   *'],
    'D': ['***  ','*  * ','*  * ','*  * ','***  '],
    'E': ['*****','*    ','*****','*    ','*****'],
    'S': ['*****','*    ','*****','    *','*****'],
    'İ': ['  *  ','     ','  *  ','  *  ','  *  '],
    'M': ['*   *','** **','* * *','*   *','*   *'],
    'T': ['*****','  *  ','  *  ','  *  ','  *  '],

    
}  # add more letters
now =""




def print_big(newList):
    for i in range(5):  # length of a list in dictionary is 5
        for j, _ in enumerate(newList):
            print(options[newList[j]][i]+"   ", end=" ")
        print()

def print_big_sec(newList):
    for i in range(5):  # length of a list in dictionary is 5
        for j, _ in enumerate(newList):
            print(options[newList[j]][i]+"   ", end=" ")
        print()


while(True):
    now = datetime.datetime.now().year
    if now == 2020:  
        name = "NOLUYO KARDESİM NE " 
        name2 ="BU TANTANA" 
        print("\n")
        print("\n")
        print_big(list(name))
        print("\n")
        print_big_sec(list(name2))
        playsound("firework3.mp3")
        playsound("noluyo.mp3")   
        playsound("2020.mp3")
        break
