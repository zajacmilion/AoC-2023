# # list = ["1aa3"]
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# char_numbers = [str(x) for x in numbers]


# list = []

# with open("1.txt", "r") as file:
#     for line in file:
#         list.append(line)


# sum = 0
# for line in list:
#     local_sum = 0
#     for char in line:
#         if char in char_numbers:
#             local_sum += int(char) * 10
#             break
#     for char in reversed(line):
#         if char in char_numbers:
#             local_sum += int(char)
#             break
#     sum += local_sum

# print(sum)



total1 = 0
total2 = 0
worNum = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7",
           "eight" : "8", "nine" : "9"}

with open("1.txt", 'r') as f:
    for line in f.readlines():

        # part 1
        chaars = [char for char in line if char.isdigit()]
        calib = int(chaars[0] + chaars[-1])
        total1 += calib


        # part 2

        s = line.strip()

        # first digit
        first_digit = None

        for i in range(len(s)):
            if s[i].isdigit():
                first_digit = s[i]
                break
            for key in worNum:
                if s[i:].startswith(key):
                    first_digit = worNum[key]
                    break
            if first_digit:
                break

        # last digit
        last_digit = None

        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                last_digit = s[i]
                break
            for key in worNum:
                if s[i:].startswith(key):
                    last_digit = worNum[key]
                    break
            if last_digit:
                print(last_digit)
                break
                


        calib = int(first_digit + last_digit)
        total2 += calib
    



print(total1)
print(total2)


