data = input().split()
print({data[x]: int(data[x + 1]) for x in range(0, len(data), 2)})

# ------------------------------------------------------(2)----------------------------
# dictionary = {}
# arr = input().split()
# for i in range(0, len(arr), 2):
#     dictionary[arr[i]] = int(arr[i + 1]) 

# print(dictionary)
