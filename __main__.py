from collections import Counter
from copy import deepcopy

from color.beaker import Beaker, Content
from color.tabular import tabulate


def print_info():
    print('All lines should have equal number of colors.')
    print(
        'Either a line can have only four characters or four group of characters separated by single space. Put 0 (zero) for empty place'
    )
    print('\nExamples:')
    print('✅ rgby')
    print('✅ r g b y')
    print('✅ red g b yel')
    print('✅ rgb0')
    print('✅ 0000')
    print('❌ red gby')
    print('❌ r  g b y')
    print('    ^^ 2 spaces')


def is_all_colors_freq_equal(shelf: list[Beaker]) -> None:
    counts: dict[Content.type, int] = {}
    for beaker in shelf:
        for content in beaker:
            if content.type in counts:
                counts[content.type] += content.size
            else:
                counts[content.type] = content.size

    size_frequency = Counter(counts.values())
    most_probable_size = max(size_frequency, key=size_frequency.get)

    print()
    flag = True
    for k, v in counts.items():
        if v != most_probable_size:
            flag = False
            print(f'{k} is present {v} times')
    return flag


def is_done(beakers: list[Beaker]) -> bool:
    i = 0
    while i < len(beakers):
        if beakers[i].is_complete():
            # print('Pop: ', beakers[i])
            beakers.pop(i)
        else:
            i += 1

    for beaker in beakers:
        if len(beaker) != 0:
            return False
    return True


def solve(shelf: list[Beaker]) -> list[str]:
    moves = []
    while not is_done(shelf):
        pouring_deadlock = True
        for i, beaker1 in enumerate(shelf, start=1):
            for j, beaker2 in enumerate(shelf, start=2):
                if beaker1 is not beaker2 and not beaker1.is_empty():
                    try:
                        beaker1.pour_into(beaker2)
                    except ValueError:
                        pass
                    else:
                        moves.append(f'{i} -> {j}')
                        pouring_deadlock = False

                    if beaker1.is_empty():
                        break

        if pouring_deadlock:
            # print('Deadlock')
            return []
    else:
        # print('Done')
        return moves


def main():
    filename = input('Enter filename: ')
    with open(filename) as f:
        inp = f.read()

    sh: list[list[str]] = tabulate(inp)
    # print(sh)

    shelf: list[Beaker] = []
    try:
        for beaker in sh:
            # '0' means empty therefore removed from beaker and as empty beaker
            while '0' in beaker:
                beaker.remove('0')
            shelf.append(Beaker(beaker))
    except ValueError:
        print('\nError: Inconsistant length in input\n')
        print_info()
        exit(1)

    # Checking if empty beaker is available or not
    for beaker in shelf:
        if beaker.is_empty():
            break
    else:
        print('No empty space available. Add empty tubes by entering 0')
        exit(1)

    # '0' is already removed
    if not is_all_colors_freq_equal(shelf):
        print('\nError: Inconsistant colors frequencies\n')
        print_info()
        exit(1)

    shortest_moves = []
    for i in range(11):
        moves = solve(deepcopy(shelf[i:] + shelf[:i]))
        if moves:
            if len(shortest_moves) == 0 or len(moves) < len(shortest_moves):
                shortest_moves = moves

    print('Solution:')
    for i, move in enumerate(shortest_moves, start=1):
        print(f'{i}:\t{move}')


if __name__ == '__main__':
    main()
