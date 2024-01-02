def green(ball : str):
    parts = ball.split(" ")
    return int(parts[0])

def red(ball : str):
    parts = ball.split(" ")
    return int(parts[0])

def blue(ball : str):
    parts = ball.split(" ")
    return int(parts[0])

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
    minG = 0
    minB = 0
    minR = 0
    # print(games_dict[game_no])
    for draw in games_dict[game_no]:
        if check != 0:
            break
        #print(draw)
        balls = draw.split(",")
        for ball in balls:
            print(ball)
            if "green" in ball:
                if green(ball.strip()) > minG:
                    minG = green(ball.strip())
            if "blue" in ball:
                if blue(ball.strip()) > minB:
                    minB = blue(ball.strip())
            if "red" in ball:
                if red(ball.strip()) > minR:
                    minR = red(ball.strip())
    print(minR, minB, minG)
    power = minR * minB * minG
    sum += power

print(sum)