people, capacity = int(input()), int(input())

if people % capacity != 0:
    print(people // capacity + 1)
else:
    print(people // capacity)

# -------------------------------------(2)----------------------
# people = int(input())
# capacity = int(input())
# counter = 0
#
# while people > capacity:
#     people -= capacity
#     counter += 1
#
# if people > 0:
#     counter += 1
#
# print(counter)


'''
17
3

output: 6
'''
