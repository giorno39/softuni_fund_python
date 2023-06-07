info = input().split(' ')
lst = []
players_team_a = 11
players_team_b = 11
condition = False

for i in info:
    if i not in lst:
        lst.append(i)
        if 'A' in i:
            players_team_a -= 1
        elif 'B' in i:
            players_team_b -= 1
        if players_team_a <= 6 or players_team_b <= 6:
            condition = True
            break

print(f'Team A - {players_team_a}; Team B - {players_team_b}')
if condition:
    print('Game was terminated')


