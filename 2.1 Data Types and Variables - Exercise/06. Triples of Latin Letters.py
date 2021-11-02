n = int(input())
[print(''.join(chr(97 + i) + chr(97 + j) + chr(97 + k)))
 for i in range(0, n)
 for j in range(0, n)
 for k in range(0, n)]


# ----------------------------------(2)-----------------------
# n = int(input())
#
# for i in range(0, n):
#   for j in range(0, n):
#     for k in range(0, n):
#
#       print(''.join((chr(97 + i),chr(97 + j),chr(97 + k))))


# -----------------------------------(3)-----------Fucking judge
# def recursion(loop, element):
#     if loop == 0:
#         print(element)
#         return
#
#     recursion(loop - 1, element + 'a')
#     recursion(loop - 1, element + 'b')
#     recursion(loop - 1, element + 'c')
#
#
# recursion(int(input()), '')
