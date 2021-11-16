data_dict = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    elif ' | ' in command:
        force_side, force_user = command.split(' | ')
        present = 0
        for k, v in data_dict.items():
            if force_user in v:
                present = 1
        if present == 0:
            if force_side not in data_dict:
                data_dict[force_side] = [force_user]
            else:
                if force_user not in data_dict[force_side]:
                    data_dict[force_side].append(force_user)
    else:
        force_user, force_side = command.split(' -> ')
        present = 0
        for k, v in data_dict.items():
            if force_user in v:
                data_dict[k].pop(v.index(force_user))
                present = 1
        if present == 1:
            if force_side not in data_dict:
                data_dict[force_side] = [force_user]
            else:
                data_dict[force_side] += [force_user]
        else:
            if force_side not in data_dict:
                data_dict[force_side] = [force_user]
            else:
                data_dict[force_side] += [force_user]
        print(f"{force_user} joins the {force_side} side!")

sort_data = dict(sorted(data_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for k, v in sort_data.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for n in sorted(v):
            print('!', n)


'''
Light | Peter
Dark | Kim
Lumpawaroo

------------------ output:

Side: Dark, Members: 1
! Kim
Side: Light, Members: 1
! Peter
'''