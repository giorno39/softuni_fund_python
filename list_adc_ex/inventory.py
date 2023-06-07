def collect_func(item):
    if item not in data:
        data.append(item)

def drop_func(item):
    if item in data:
        data.remove(item)

def renew_func(item):
    if item in data:
        data.remove(item)
        data.append(item)

def combine_func(item):
    collectables = item.split(':')
    old_item = collectables[0]
    new_item = collectables[1]
    if old_item in data:
        a = data.index(old_item)
        data.insert(a + 1, new_item)


data = input().split(', ')

command = input()

while command != 'Craft!':
    explosion = command.split(' - ')
    current_command = explosion[0]
    item = explosion[1]
    if current_command == 'Collect':
        collect_func(item)

    if current_command == 'Drop':
        drop_func(item)

    if current_command == "Renew":
        renew_func(item)

    if current_command == 'Combine Items':
        combine_func(item)
    command = input()

print(", ".join(data))

