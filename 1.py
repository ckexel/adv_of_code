inventory = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'


f = open('1_inventory.txt', 'r')
inventory = f.read()


def most_calories(inv):
    calories_list = [elf.split('\n') for elf in inv.split('\n\n')]
    calories_list = [[int(cal) for cal in elf] for elf in calories_list]
    sums = [sum(elf) for elf in calories_list]
    return max(sums)


def most3_calories(inv):
    calories_list = [elf.split('\n') for elf in inv.split('\n\n')]
    calories_list = [[int(cal) for cal in elf] for elf in calories_list]
    sums = [sum(elf) for elf in calories_list]
    sums.sort(reverse=True)
    return sum(sums[:3])


print(most_calories(inventory))
print(most3_calories(inventory))
