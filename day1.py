import numpy as np

from util import parse_input

if __name__ == '__main__':
    data = parse_input('data/day1.txt')

    calories = []
    count = 0
    for entry in data:
        if entry != '':
            count += int(entry)
        else:
            calories.append(count)
            count = 0

    print(np.array(calories).max())

    # part 2:

    top3 = np.array(calories)
    top3[::-1].sort()
    print(sum(top3[:3]))