n = int(input())
wagons_list = [0] * n

while True:
    command, *nums = input().split()
    if command == 'End':
        break

    if command == 'add':
        wagons_list[n - 1] += int(nums[0])
    elif command == 'insert':
        wagons_list[int(nums[0])] += int(nums[1])
    else:
        wagons_list[int(nums[0])] -= int(nums[1])

print(wagons_list)

'''
3
add 20
insert 0 15
leave 0 5
End

output: [10, 0, 20]
'''
