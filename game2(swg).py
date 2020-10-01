import random

least = ['s', 'w', 'g']
var = 0
pc_point = 0
user_point = 0
chance = 10


print()
print(" * * * * * * * WELCOME TO SnAkE , WAtEr , GuN    GAME  * * * * * * * * * *")
print()
print('TOTAL CHANCE = ',chance)
print()

while var < chance:
    user_inp = input("enter s , w or g any one can enter :- ")
    rd = random.choice(least)
    if user_inp == rd:
        chance -= 1
        print("  TIED  ")
        print('left only : ', chance)
        print()

    elif user_inp == 's' and rd == 'w':
        chance -= 1
        user_point += 1
        print("one point to user ")
        print('left only : ', chance)
        print()

    elif user_inp == 's' and rd == 'g':
        chance -= 1
        pc_point += 1
        print("one point to pc")
        print('left only : ', chance)
        print()

    elif user_inp == 'w' and rd == 's':
        chance -= 1
        pc_point += 1
        print('one point to pc')
        print('left only : ', chance)
        print()

    elif user_inp == 'w' and rd == 'g':
        chance -= 1
        pc_point +=1
        print('one point to pc')
        print('left only : ', chance)
        print()

    elif user_inp == 'g' and rd == 's':
        chance -= 1
        user_point += 1
        print("one point to user")
        print('left only : ', chance)
        print()

    elif user_inp == 'g' and rd == 'w':
        chance -= 1
        user_point += 1
        print("one point to pc")
        print('left only : ', chance)
        print()
    
    elif chance==0:
        print('GAME OVER ')
        print()
    else:
        print("PLEASE DON'T ENTER ANY CHARACTER")
        chance -= 1
        print('left only : ', chance)
        print()
    
if user_point > pc_point:
    print("CONGRATULATIONS you are WIN ")
    print('your score is : ', user_point)
    print()

else:
        print('Bad LuCk pc win ')
        print("pc's score is : ", pc_point)
        print()


print('* * * * * * * * * *    THANK YOU FOR PLAYING * * * * * * * * * ')
