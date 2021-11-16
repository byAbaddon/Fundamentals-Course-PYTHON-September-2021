players_dict = {}

while True:
    try:
        user, hat, pts = [int(i) if i.isdigit() else i for i in input().split(' <:> ')]

        if hat not in players_dict:
            players_dict[hat] = {user: pts}
        if user not in players_dict[hat]:
            players_dict[hat].update({user: pts})
        if pts > players_dict[hat][user]:
            players_dict[hat][user] = pts
    except:
        break

sort_list = []
for key, val in players_dict.items():
    for k, v in val.items():
        sort_list.append([k, v, len(val), key])
sort_list = sorted(sort_list, key=lambda x: (-x[1], -x[2]))
for el in sort_list:
    print(f"({el[3]}) {el[0]} <-> {el[1]}")

'''
Pesho <:> Red <:> 2000
Tosho <:> Blue <:> 1000
Gosho <:> Green <:> 1000
Sasho <:> Yellow <:> 4500
Prakasho <:> Stamat <:> 1000
Once upon a time

---------------------------output:
(Yellow) Sasho <-> 4500
(Red) Pesho <-> 2000
(Blue) Tosho <-> 1000
(Green) Gosho <-> 1000
(Stamat) Prakasho <-> 1000

'''