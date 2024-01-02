def green(ball : str):
    parts = ball.split(" ")
    if int(parts[0]) <= 13:
        return True
    return False

def red(ball : str):
    parts = ball.split(" ")
    if int(parts[0]) <= 12:
        return True
    return False

def blue(ball : str):
    parts = ball.split(" ")
    if int(parts[0]) <= 14:
        return True
    return False

games = []

with open("2.txt") as file:
    for line in file:
        games.append(line)

games_dict = {}
for game in games:
    parts = game.split(":")
    games_dict[int(parts[0].replace("Game ", ""))] = parts[1].strip().split(";")

sum = 0
for game_no in games_dict:
    print(game_no)
    check = 0
    # print(games_dict[game_no])
    for draw in games_dict[game_no]:
        if check != 0:
            break
        #print(draw)
        balls = draw.split(",")
        for ball in balls:
            print(ball)
            if "green" in ball:
                if not green(ball.strip()):
                    check += 1000
                    break
            elif "red" in ball:
                if not red(ball.strip()):
                    check += 1000
                    break
            elif "blue" in ball:
                if not blue(ball.strip()):
                    check += 1000
                    break
    if check == 0:
        sum += game_no

print(sum)
