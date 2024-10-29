import random


players = [1, 3, 18, 9]

assigned = players.copy()

random.shuffle(assigned)

print(assigned)

successful_assignment = False
while successful_assignment == False:
    successful_assignment = True
    for i in range(len(players)):
        if players[i] == assigned[i]:
            successful_assignment = False
            random.shuffle(assigned)
            break

print(assigned)



