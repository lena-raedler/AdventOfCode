from enum import Enum
from util import parse_input

# data = ['A Y', 'B X', 'C Z']
data = parse_input('data/day2.txt')
data.pop(-1)


class GameEnd(Enum):
    DRAW = 3
    LOSS = 0
    WIN = 6


class SELECTION(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


count = 0
game_state_array = []

for entry in data:
    match entry[0]:
        case 'A':   # rock
            if entry[2] == 'X':  # rock
                count += 1
                game_state_array.append(GameEnd.DRAW)
            elif entry[2] == 'Y':   # paper
                count += 2
                game_state_array.append(GameEnd.WIN)
            else:   # scissors
                count += 3
                game_state_array.append(GameEnd.LOSS)

        case 'B':   # paper
            if entry[2] == 'X':  # rock
                count += 1
                game_state_array.append(GameEnd.LOSS)
            elif entry[2] == 'Y':  # paper
                count += 2
                game_state_array.append(GameEnd.DRAW)
            else:  # scissors
                count += 3
                game_state_array.append(GameEnd.WIN)
        case 'C':   # scissors
            if entry[2] == 'X':  # rock
                count += 1
                game_state_array.append(GameEnd.WIN)
            elif entry[2] == 'Y':  # paper
                count += 2
                game_state_array.append(GameEnd.LOSS)
            else:  # scissors
                count += 3
                game_state_array.append(GameEnd.DRAW)

print(game_state_array)
print(count)
for entry in game_state_array:
    count += entry.value

print(count)

count = 0
game_state_array = []
for entry in data:
    match entry[0]:
        case 'A':   # rock
            if entry[2] == 'X':  # loss
                count += SELECTION.SCISSORS.value
                game_state_array.append(GameEnd.LOSS)
            elif entry[2] == 'Y':   # draw
                count += SELECTION.ROCK.value
                game_state_array.append(GameEnd.DRAW)
            else:   # win
                count += SELECTION.PAPER.value
                game_state_array.append(GameEnd.WIN)

        case 'B':   # paper
            if entry[2] == 'X':  # loss
                count += SELECTION.ROCK.value
                game_state_array.append(GameEnd.LOSS)
            elif entry[2] == 'Y':  # draw
                count += SELECTION.PAPER.value
                game_state_array.append(GameEnd.DRAW)
            else:  # win
                count += SELECTION.SCISSORS.value
                game_state_array.append(GameEnd.WIN)
        case 'C':   # scissors
            if entry[2] == 'X':  # loss
                count += SELECTION.PAPER.value
                game_state_array.append(GameEnd.LOSS)
            elif entry[2] == 'Y':  # draw
                count += SELECTION.SCISSORS.value
                game_state_array.append(GameEnd.DRAW)
            else:  # win
                count += SELECTION.ROCK.value
                game_state_array.append(GameEnd.WIN)

for entry in game_state_array:
    count += entry.value

print(count)