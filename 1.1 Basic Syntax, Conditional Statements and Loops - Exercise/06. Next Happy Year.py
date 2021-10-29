print([year for year in range(int(input()) + 1, 99999) if len(set(str(year))) == len(str(year))][0])


# ---------------------------------------(2)----------------------------------
# years = int(input()) + 1
#
# for year in range(years, 99999):
#     if len(set(str(year))) == len(str(year)):
#         print(year)
#         break


#---------------------------------------(3)---------------------

# year = int(input()) + 1
# while len(set(str(year))) != len(str(year)):
#     year += 1
#
# print(year)

'''
8989
output: 9012
'''
