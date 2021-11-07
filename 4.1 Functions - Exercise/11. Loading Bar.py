loading = int(input())
if loading == 100:
    print(f'100% Complete!\n[%%%%%%%%%%]')
else:
    bar = ['%'] * int(100 * (loading / 1000))
    bar.extend('.' * (10 - len(bar)))
    print(f'{loading}%', '[' + ''.join(bar) + ']')
    print('Still loading...')

# 30
