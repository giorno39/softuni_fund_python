followers = {}


while True:
    command = input()

    if command == "Log out":
        break

    explode = command.split(": ")
    type_of_command = explode[0]

    if type_of_command == "New follower":
        username = explode[1]
        if username not in followers:
            followers[username] = list()
            followers[username].append(0)
            followers[username].append(0)

    if type_of_command == "Like":
        username = explode[1]
        count = int(explode[2])
        if username not in followers:
            followers[username] = list()
            followers[username].append(count)
            followers[username].append(0)
        else:
            followers[username][0] += count

    if type_of_command == "Comment":
        username = explode[1]
        if username not in followers:
            followers[username] = list()
            followers[username].append(0)
            followers[username].append(1)
        else:
            followers[username][1] += 1

    if type_of_command == "Blocked":
        username = explode[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)


print(f"{len(followers)} followers")

for follower in followers.keys():
    value_of_follower = followers[follower][0] + followers[follower][1]
    print(f"{follower}: {value_of_follower}")

