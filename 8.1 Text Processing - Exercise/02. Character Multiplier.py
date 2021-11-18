str1, str2 = input().split()
total_sum = 0

for i in range(50):
    try:
        total_sum += ord(str1[i]) * ord(str2[i])
    except:
        if len(str1) < len(str2):
            big_str = str2[len(str1):]
        else:
            big_str = str1[len(str2):]

        for j in range(len(big_str)):
            total_sum += ord(big_str[j])
        break

print(total_sum)

# --------------------------------------FUCKING JUDGE---------(2)-----------------------
# str1, str2 = input().split()
# total_sum = 0
#
# for i in range(50):
#     try:
#         total_sum += ord(str1[i]) * ord(str2[i])
#     except:
#         if len(str1) < len(str2):
#             total_sum += ord(str2[i])
#         else:
#             total_sum += ord(str1[i])
#     finally:
#         continue  # ----Judge throw error----------python 3.8 suport this-------not Judge-------------
#
# print(total_sum)
