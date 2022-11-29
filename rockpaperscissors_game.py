import random
print("Computer's Turn: Scissor(s) Paper(p) Rock(r) ?")

randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
else:
    comp="r"

you=input("Your Turn: Scissor(s) Paper(p) Rock(r) ?")
print(f"Computer chose {comp}")
print(f"You chose {you}")
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True

a=gameWin(comp,you)
if a==None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
