import re

number_of_bosses = int(input())

for boss in range(number_of_bosses):
    data = input()
    pattern = r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#"

    matches = re.findall(pattern, data)

    if matches:
        print(f"{matches[0][0]}, The {matches[0][1]}")
    else:
        print("Access denied!")

    other_matches = re.finditer(pattern, data)

    for match in other_matches:
        print(f">> Strength: {len(match.group(1))}")
        print(f">> Armor: {len(match.group(2))}")



