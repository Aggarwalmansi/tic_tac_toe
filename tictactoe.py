import os

ls = [1,2,3,4,5,6,7,8,9]

def pattern():
    k = 0
    os.system('clear') 
    for i in range(13):
        for j in range(13):
            if (i == 2 or i == 6 or i == 10) and (j == 2 or j == 6 or j == 10):
                print(ls[k], end=" ")
                k += 1
            elif i == 4 or i == 8 or j == 4 or j == 8:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def verify(x):
    a = ['1','2','3','4','5','6','7','8','9']
    if x not in a:
        return False
    x = int(x)
    if ls[x - 1] == 'X' or ls[x - 1] == "O":
        return False
    return True  

def update(x, i):
    if i % 2 == 0:
        ls[x - 1] = "X"
    else:
        ls[x - 1] = "O"

def is_won():
    if ls[0] == ls[1] == ls[2]:
        return True
    elif ls[3] == ls[4] == ls[5]:
        return True
    elif ls[6] == ls[7] == ls[8]:
        return True
    elif ls[0] == ls[3] == ls[6]:
        return True
    elif ls[1] == ls[4] == ls[7]:
        return True
    elif ls[2] == ls[5] == ls[8]:
        return True
    elif ls[0] == ls[4] == ls[8]:
        return True
    elif ls[2] == ls[4] == ls[6]:
        return True
    return False  # Ensure it returns False if no win condition is met

def is_tie():
    for x in ls:
        if x not in ["X", "O"]:  # agr puri list me koi bhi element bacha hai jo na X ho na O
            return False  
    return True  # If all positions are filled and no one has won, it's a tie

# game start
pattern() 
i = 0 
while i < 9:
    if i % 2 == 0:
        print("User 1 Turn")
    else:
        print("User 2 Turn")

    print("Enter your choice (1-9):", end=" ")
    z = input()
    y = verify(z)

    if not y:
        pattern()
        print("Invalid Choice. Please Try Again")
        continue

    update(int(z), i)
    i += 1  #  next turn
    pattern()

    if is_won():
        if i % 2 == 0:
            print("User 1 Won 🏆")

        else:
            print("User 2 Won 🏆")
        break  

    if is_tie(): 
        print("It's a Tie! No one wins.👻retry")
        break