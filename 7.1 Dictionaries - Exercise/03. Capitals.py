capitals_dict = dict(zip(
    [capital for capital in input().split(', ')],
    [city for city in input().split(', ')]))

[print(f'{k} -> {v}') for k, v in capitals_dict.items()]

'''
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London

output:
Bulgaria -> Sofia
Romania -> Bucharest
Germany -> Berlin
England -> London
'''
