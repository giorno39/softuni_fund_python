ppl_waiting = int(input())
wagons = list(map(int, input().split(" ")))

for i in range(len(wagons)):
    while wagons[i] < 4:
        if ppl_waiting == 0:
            break
        new_wagon = wagons[i] + 1
        wagons[i] = new_wagon
        ppl_waiting -= 1

if sum(wagons) < (4 * len(wagons)):
    print("The lift has empty spots!")
if ppl_waiting != 0:
    print(f"There isn't enough space! {ppl_waiting} people in a queue!")

wagons = map(str, wagons)
output = " ".join(wagons)
print(output)




