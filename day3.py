from util import parse_input

# data = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#         'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

data = parse_input('data/day3.txt')


def get_value(letter : str):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return get_value(letter.lower()) + 26


if __name__ == '__main__':

    priority_items = []
    for entry in data:
        divider = len(entry) // 2
        part1 = entry[:divider]
        part2 = entry[divider:]
        priority_item = set()
        for letter in part1:
            if letter in part2:
                priority_item.add(letter)

        priority_items.append(priority_item)

    count = 0
    for item in priority_items:
        for value in item:
            count += get_value(value)

    print(count)

    # part 2
    data_triples = []
    triple = []
    for i in range(len(data)):
        if i % 3 == 0 and i != 0:
            data_triples.append(triple)
            triple = []
            triple.append(data[i])
        if i % 3 != 0 or i == 0:
            triple.append(data[i])

    data_triples.append(triple)

    common_letters = []
    for triple in data_triples:
        common_letter = []
        for letter in triple[0]:
            if letter in triple[1] and letter in triple[2] and letter not in common_letter:
                common_letter.append(letter)
        common_letters.append(common_letter)

    count = 0
    for letter in common_letters:
        if letter == []:
            continue
        count += get_value(letter[0])

    print(count)

