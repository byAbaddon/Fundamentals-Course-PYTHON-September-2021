notes_list = [0] * 10

while True:
    try:
        index, note = input().split('-')
        notes_list.insert(int(index), note)
        notes_list.remove(0)
    except:
        print([note for note in notes_list if not note == 0])
        break

# ------------------------(2)-----------------TODO:  80pts

# to_do_dict = {k: v for k, v in [k.split('-') for k in iter(input, 'End')]}
# print([v for k, v in sorted(to_do_dict.items(), key=lambda item: item[0])])

'''
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End

output: ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
'''
