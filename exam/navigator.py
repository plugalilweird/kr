def Navigator(commands):
    total = 0
    for command in commands:
        for index in range(len(command)):
            if command[index].isdigit():
                start = index
                while index < len(command) and (command[index].isdigit() or command[index] == '.'):
                    index += 1
                num = float(command[start:index])
                if command[index:index+2] == 'km':
                    num = float(command[start:index]) * 1000
                if command[index:index + 1] == 'm':
                    num = command[start:index]
                total += int(num)
                break
    return total

commands = [
    "100m to intersection",
    "turn right",
    "straight 300m",
    "enter motorway",
    "straight 5.3km",
    "exit motorway",
    "500m straight",
    "turn sharp left",
    "continue 100m to destination"
]

print(Navigator(commands))
