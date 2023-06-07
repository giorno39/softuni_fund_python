# 30% [%%%.......]
# Still loading...

n = int(input())
if n == 100:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
else:
    perc = n // 10 * '%'
    dots = (10 - (n//10)) * '.'
    print(f'{n}% [{perc}{dots}]')
    print('Still loading...')
