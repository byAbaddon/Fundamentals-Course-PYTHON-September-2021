import os
os.system('clear')

pirateShip = [int(i) for i in input().split('>')]
battleShip = [int(i) for i in input().split('>')]
maxHP = int(input())
pirateShipStatus = 0
battleShipStatus = 0
while pirateShipStatus == battleShipStatus:
    command = input()
    if command == 'Retire':
        print(f"Pirate ship status: {sum(i for i in pirateShip)}")
        print(f"Warship status: {sum(i for i in battleShip)}")
        break
    else:
        commandSplit = command.split(' ')
        subcom = commandSplit[0]
        if subcom == 'Fire':
            fireIndex = int(commandSplit[1])
            fireDamage = int(commandSplit[2])
            if 0 <= fireIndex < len(battleShip):
                battleShip[fireIndex] -= fireDamage
                if battleShip[fireIndex] <= 0:
                    print(f"You won! The enemy ship has sunken.")
                    battleShipStatus = 1
        elif subcom == 'Defend':
            fireStartIndex = int(commandSplit[1])
            fireEndIndex = int(commandSplit[2])
            fireDamage = int(commandSplit[3])
            if 0 <= fireStartIndex < len(pirateShip) and 0 <= fireEndIndex < len(pirateShip):
                for i in range(fireStartIndex, fireEndIndex + 1):
                    pirateShip[i] -= fireDamage
                    if pirateShip[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        pirateShipStatus = 1
                        break
        elif subcom == 'Repair':
            repairIndex = int(commandSplit[1])
            repairDamage = int(commandSplit[2])
            if 0 <= repairIndex < len(pirateShip):
                if (pirateShip[repairIndex] + repairDamage) > maxHP:
                    pirateShip[repairIndex] = maxHP
                else:
                    pirateShip[repairIndex] += repairDamage
        elif subcom == 'Status':
            perc = maxHP * 0.2
            print(f"{sum(1 for i in pirateShip if i < perc)} sections need repair.")



#---------------------------------------(2)----------------------------------------(80pts) TODO


# pirate_ship = list(map(int ,input().split('>')))
# war_ship = list(map(int ,input().split('>')))
# health = int(input())

# finish_progam = False

# while True:
#     tokens = input()
#     if len(tokens) == 6:
#         command = tokens
#     else:
#         tokens = tokens.split(' ')
#         command = tokens[0] 

#     if command == 'Retire':
#         break

#     if command == 'Status':
#         count = [pirate_ship[el] for el in range(len(pirate_ship))  if pirate_ship[el] < (health * 0.20) ]
#         print(f'{len(count)} sections need repair.')
#         continue
       
#     index =  int(tokens[1])
#     demage = int(tokens[2])

#     if command == 'Fire':
#         if 0 <= len(war_ship ) > index:
#              war_ship [index] -= demage
#              if war_ship [index] <= 0:
#                  print('You won! The enemy ship has sunken.')
#                  finish_progam = True
#                  break
#     elif command == 'Repair':
#         if 0 <= len(pirate_ship) > index:
#             repair = demage
#             pirate_ship[index] += demage
#             if pirate_ship[index] > health:
#                 pirate_ship[index] = health
#     elif command == 'Defend':
#         start_index = int(index)
#         end_index =  int(demage)
#         demage = int(tokens[3])
#         if (start_index >= 0  and start_index < len(pirate_ship)) and ( end_index > start_index and end_index < len(pirate_ship)):
#             for i in range(start_index, end_index + 1):
#                 pirate_ship[i] -= demage
#                 if pirate_ship[i] <= 0: 
#                     print('You lost! The pirate ship has sunken.')
#                     finish_progam = True
#                     break

# if finish_progam == False:
#     print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}')






