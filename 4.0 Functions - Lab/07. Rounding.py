def round_function(numbers):
    return [round(float(x)) for x in numbers]
    # return list(map(lambda x: round(float(x)), numbers))


print(round_function((input().split())))

# 1.0 2.5 3.0 4.5
# output: [1, 2, 3, 4]
