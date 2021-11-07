def password_validator(string):
    length = 6 <= len(string) <= 10
    count_digits = 0
    wrong_char = False

    for i in string:
        if 48 <= ord(i) <= 57:
            count_digits += 1
        if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57):
            wrong_char = True

    if length and count_digits >= 2 and wrong_char is False:
        print('Password is valid')
    else:
        if length is False:
            print('Password must be between 6 and 10 characters')
        if wrong_char:
            print('Password must consist only of letters and digits')
        if count_digits < 2:
            print('Password must have at least 2 digits')


password_validator(input())

# logIn
