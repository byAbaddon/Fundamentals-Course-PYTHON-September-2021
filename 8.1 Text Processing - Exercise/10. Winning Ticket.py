tickets = input()
tickets_list = tickets.replace(' ', '').split(',')

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:

    if len(ticket) != 20:
        print('invalid ticket')
        continue

    else:
        left_half = ticket[0:10]
        right_half = ticket[10:20]
        left_half_match = False
        right_half_match = False
        match_symbol = ''
        match_length = 0
        match_length_left = 0
        match_length_right = 0

        for symbol in winning_symbols:
            if symbol in left_half:
                left_sequence = 0
                right_sequence = 0

                for char in left_half[left_half.index(symbol):]:
                    if char == symbol:
                        left_sequence += 1
                        if left_sequence >= 6:
                            match_length_left = left_sequence
                            left_half_match = True
                    else:
                        left_sequence = 0

                if left_half_match:
                    for char in right_half[right_half.index(symbol):]:
                        if char == symbol:
                            right_sequence += 1
                            if right_sequence >= 6:
                                match_length_right = right_sequence
                                right_half_match = True
                        else:
                            right_sequence = 0

                if left_half_match and right_half_match:
                    match_symbol = symbol
                    if match_length_left > match_length_right:
                        match_length = match_length_right
                    elif match_length_left < match_length_right:
                        match_length = match_length_left
                    elif match_length_left == match_length_right:
                        match_length = match_length_left

                    if 6 <= match_length <= 9:
                        print(f'ticket "{ticket}" - {match_length}{match_symbol}')
                    elif match_length == 10:
                        print(f'ticket "{ticket}" - {match_length}{match_symbol} Jackpot!')
                    break
        else:
            print(f'ticket "{ticket}" - no match')



# -------------------------------------------(2)------TODO: 63pts--------------------
# import re
#
# tickets_list = input().replace(' ', '').split(',')
# pattern = ['@', '#', "$", '^']
# symbol = ''
# ticket_count = 0
# regex = r'([@|#|$|\^]{1,})'
#
# for ticket in tickets_list:
#     if len(ticket) != 20:
#         print('invalid ticket')
#         continue
#     else:
#         left_part = list(filter(lambda x: x in pattern, ticket[0:10]))
#         right_part = list(filter(lambda x: x in pattern, ticket[10:20]))
#
#         left_size = re.findall(regex, ticket[:10])
#         right_size = re.findall(regex, ticket[10:])
#
#         if left_part != [] or right_part != []:
#             if len(left_size) > 1:
#                 ticket_count = len(sorted(left_size, reverse=True)[0])
#             else:
#                 ticket_count = len(sorted(right_size, reverse=True)[0])
#
#         else:
#             is_equals_all_symbols = len(set(left_part)) == 1  # True or  False
#             print(f'ticket "{ticket}" - no match')
#             continue
#
#         if len(left_part) == len(right_part) and len(left_part) == 10:
#             print(f'ticket "{ticket}" - 10{left_part[0]} Jackpot!')
#         elif len(left_part):
#             symbol = set(left_part).pop()
#             print(f'ticket "{ticket}" - {ticket_count}{symbol}')

'''
Cash$$$$$$Ca$$$$$$sh
Cash111111Ca111111sh
'''