numbers_list = [int(input()) for x in range(int(input()))]
neg_list = [x for x in numbers_list if x < 0]
pos_list = [x for x in numbers_list if x > 0]

print(f'{pos_list}\n{neg_list}')
print(f'Count of positives: {len(pos_list)}\nSum of negatives: {sum(neg_list)}')

# ------------------------------(2)----------------------------------------------

# n = int(input())
# pos_list = []
# neg_list = []
#
# for _ in range(n):
#     current = int(input())
#     if current >= 0:
#         pos_list.append(current)
#     else:
#         neg_list.append(current)
#
# print(f'{pos_list}\n{neg_list}')
# print(f'Count of positives: {len(pos_list)}\nSum of negatives: {sum(neg_list)}')


'''
5
10
3
2
-15
-4

'''
