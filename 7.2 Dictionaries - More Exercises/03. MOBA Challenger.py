playersDict = {}
totalSkillDict = {}

while True:
    command = input()
    if command == 'Season end':
        break
    else:
        if '->' in command:
            comSplit = command.split(' -> ')
            player, position, skill = comSplit[0], comSplit[1], int(comSplit[2])
            if player not in playersDict:
                playersDict[player] = {position: skill}
                totalSkillDict[player] = skill
            else:
                if position not in playersDict[player]:
                    playersDict[player][position] = skill
                    totalSkillDict[player] += skill
                else:
                    if playersDict[player][position] < skill:
                        playersDict[player][position] = skill
                        totalSkillDict[player] += skill - playersDict[player][position]
        elif ' vs ' in command:
            comSplit = command.split(' vs ')
            player1, player2 = comSplit[0], comSplit[1]
            if player1 in totalSkillDict and player2 in totalSkillDict:
                commonPosition = False
                for i in playersDict[player1].keys():
                    if i in playersDict[player2]:
                        commonPosition = True
                        break
                if commonPosition is True:
                    if totalSkillDict[player1] > totalSkillDict[player2]:
                        del playersDict[player2]
                        del totalSkillDict[player2]
                    elif totalSkillDict[player1] < totalSkillDict[player2]:
                        del playersDict[player1]
                        del totalSkillDict[player1]
sortedSkillDict = dict(sorted(totalSkillDict.items(), key=lambda x: (-x[1], x[0])))
sortedPlayerDict = {}
for k, v in sortedSkillDict.items():
    print(f"{k}: {v} skill")
    for c, b in sorted(playersDict[k].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {c} <::> {b}")

# ----------------------------------(2)---------TODO------------------80 pts   runtime error ???
# challenger_dict = {}
# ranking_dict = {}
#
# while True:
#     token = input()
#     if token == 'Season end':
#         break
#     elif '->' in token:
#         name, skill, pts = [int(x) if x.isdigit() else x for x in token.split(' -> ')]
#         if name not in challenger_dict:
#             challenger_dict[name] = {skill: pts}
#             ranking_dict[name] = pts
#         else:
#             if skill not in challenger_dict[name]:
#                 challenger_dict[name].update({skill: pts})
#                 ranking_dict[name] += pts
#             if pts > challenger_dict[name][skill]:
#                 challenger_dict[name][skill] = pts
#     else:
#         player_name_one, player_name_two = token.split(' vs ')
#         if player_name_one in challenger_dict and player_name_two in challenger_dict:
#             for key, val in challenger_dict[player_name_one].items():
#                 if key in challenger_dict[player_name_one] and key in challenger_dict[player_name_two]:
#                     if challenger_dict[player_name_one][key] < challenger_dict[player_name_two][key]:
#                         del challenger_dict[player_name_one]
#                         del ranking_dict[player_name_one]
#                     elif challenger_dict[player_name_one][key] > challenger_dict[player_name_two][key]:
#                         del challenger_dict[player_name_two]
#                         del ranking_dict[player_name_two]
#
# sort_ranking_dict = dict(sorted(ranking_dict.items(), key=lambda x: (-x[1], x[0])))
#
# for key, val in sort_ranking_dict.items():
#     print(f'{key}: {val} skill')
#     sort_challenger_pts = dict(sorted(challenger_dict[key].items(), key=lambda x: (-x[1], x[0])))
#     for name, pts in sort_challenger_pts.items():
#         print(f'- {name} <::> {pts}')


'''
Pesho -> Adc -> 400
Gosho -> Jungle -> 300
Stamat -> Mid -> 200
Stamat -> Support -> 250
Season end

--------------------- output:
Stamat: 450 skill
- Support <::> 250
- Mid <::> 200
Pesho: 400 skill
- Adc <::> 400
Gosho: 300 skill
- Jungle <::> 300
'''