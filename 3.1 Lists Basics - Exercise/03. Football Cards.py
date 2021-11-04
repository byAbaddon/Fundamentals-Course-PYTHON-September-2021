players_list = list(set(input().split()))
team_A = team_B = 11

for i in range(1, 12):
    team_A -= int(players_list.count(f"A-{i}"))
    team_B -= int(players_list.count(f"B-{i}"))
    if team_A < 7 or team_B < 7:
        print(f'Team A - {team_A}; Team B - {team_B}\nGame was terminated')
        exit()

print(f"Team A - {team_A}; Team B - {team_B}")


# -------------------------------(2)-------TODO: 80pts  --------------------------------------------
# from re import findall
#
# coll_list = ''.join(set(input().split(' ')))
# a_players = 11 - len(findall(r'A+', coll_list))
# b_players = 11 - len(findall(r'B+', coll_list))
# print(f'Team A - {a_players}; Team B - {b_players}')
# print('Game was terminated') if a_players < 7 or b_players < 7 else f'Team A - {a_players}; Team B - {b_players}'


'''
A-1 A-5 A-10 B-2
'''
