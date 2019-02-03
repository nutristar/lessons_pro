import random
print("---Game---")
print("Stone/Scissors/Paper")

ap=random.randint(1,3)
if ap ==1:
    gg="Stone"
elif ap==2:
    gg="Scissors"
elif ap==3:
    gg="Paper"

print(gg)
you=input("пиши  Stone  Scissors или Paper.....")

if you==gg:
    print("ничья")
elif you=="Stone" and  gg=="Scissors":
    print("you win")
elif you=="Stone" and  gg=="Paper":
    print("you lose")
elif you=="Scissors" and gg=="Stone":
    print("Ti   LOX")
elif you=="Scissors" and gg=="Paper":
    print("YOU  WIN")
elif you=="Paper" and gg=="Stone":
    print("YOU WIN")
elif you=="Paper" and gg=="Scissors":
    print("Ti LOX")

