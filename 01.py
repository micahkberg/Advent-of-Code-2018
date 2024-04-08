def load():
    with open("inputs/01.txt") as f:
        lines = f.read().strip()
        return lines.split("\n")


def main():
    frequencies = load()
    freq = 0
    seen_freq = set()
    part1=True
    part2_solution = None
    while not part2_solution:
        for line in frequencies:
            seen_freq.add(freq)
            freq += eval(line)
            if freq in seen_freq:
                part2_solution = freq
                break
        if part1:
            print('part1')
            print(freq)
            part1=False
    print('part2')
    print(part2_solution)


main()
