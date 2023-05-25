sheeps = list(reversed(input().split(', ')))
print('Please go away and stop eating my sheep' if sheeps[0] == 'wolf' else f'Oi! Sheep number {sheeps.index("wolf")}! You are about to be eaten by a wolf!')
#-------------------------------------------------(2)----------------------------------------

sheep_list = list(reversed(input().split(', ')))

if sheep_list[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    index = sheep_list.index('wolf')
    print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')

    # wolf, sheep, sheep, sheep, sheep, sheep
    # sheep, sheep, wolf, sheep, sheep, sheep
