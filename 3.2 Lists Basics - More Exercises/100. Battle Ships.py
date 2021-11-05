#--------------------------------------------------------------100pts------------------------------------
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
attack = input().split()
count_destroyed_ship = 0

for i in range(len(attack)):
    row, col= list(map(int,(attack[i].split('-'))))

    if arr[row][col] > 0:
        arr[row][col] -= 1 
        if arr[row][col] == 0:
            count_destroyed_ship += 1
       
print(count_destroyed_ship)   



#------------------------------------Fucking Judge (Time limit) -----------------------------
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# attack = input().split()
# count_destroyed_ship = 0

# while attack:
#     for row in range(len(arr)):
#         for col in range(len(arr)):
#             current = attack[0].split('-')
#             row_pos = int(current[0])
#             col_pos = int(current[1])

#             if row_pos == row and col_pos == col:
#                 attack.pop(0)
#                 if len(attack) == 0:
#                     break    

#                 if int(arr[row][col]) > 0:
#                     arr[row][col] -= 1 
#                     if arr[row][col] == 0:
#                         count_destroyed_ship += 1
#                     else:
#                         break

# print(count_destroyed_ship)        
