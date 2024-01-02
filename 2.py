sum_num = 0
limit = {"red":12, "green":13, "blue":14}
sum_powers = 0

# part 1
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        impossible = False
        picks = line.strip()[line.find(":") + 2:].split("; ")
        for p in picks:
            for part in p.split(", "):
                num, color = part.split(" ")
                num = int(num)
                if limit[color] < num:
                    impossible = True
                    break
                if impossible:
                    break
        if not impossible:
            sum_num += i+1

print(sum_num)



# part 2
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        impossible = False
        picks = line.strip()[line.find(":") + 2:].split("; ")
        min_possible = {'red': 0, 'green': 0, 'blue': 0}
        for p in picks:
            for part in p.split(", "):
                num, color = part.split(" ")
                num = int(num)
                min_possible[color] = max(min_possible[color], num)
        power = 1
        for v in min_possible.values():
            power *= v
        sum_powers += power

print(sum_powers)