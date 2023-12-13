path = './day2.txt'

colorLimits = {
    "blue": 14,
    "red": 12,
    "green": 13
}

validSum = 0
powerSum = 0

with open(path, 'r') as fp:
    for line in fp.readlines():

        maxColors = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        validGame = True
        game = line.split(':')
        game_id = int(game[0].replace("Game ", ""))
        
        # review each draw of cubes, check if possible
        for draw in game[1].split(';'):
            for cube in draw.split(','):
                number, color = cube.strip().split(' ')
                number = int(number)
                if colorLimits[color] < number:
                    validGame = False  

                if maxColors[color] < number:
                    maxColors[color] = number 

        if validGame:
            validSum += game_id

        powerSum += maxColors['red'] * maxColors['blue'] * maxColors['green']

print(powerSum)