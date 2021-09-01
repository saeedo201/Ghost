from random import randint
print(3*"\t","ghost game")
score = 0
while True:
    ghost_room = randint(1,3)
    print("three rooms ahead ==> ghost behind one of them")
    print("choice which room to open")
    print("choice room of 1 to 3")
    room = int(input("whate you choice: "))
    if room == ghost_room:
        break
    elif room > 3:
        print("out of rooms")
        break
    elif room < 0:
        print("out of rooms")
        break
    else:
        print("the ghost not here.. good")
        print("enter next room")
        score += 1
print("run a way the ghost behind you")
print("game over! your score is: ", score)