import itertools

def load():
    with open("inputs/02.txt") as f:
        lines = f.read().strip()
        return lines.split("\n")


def main():
    ids = load()
    count2 = 0
    count3 = 0
    for id_str in ids:
        add_to_count2 = False
        add_to_count3 = False
        letters = set(id_str)
        for letter in letters:
            if id_str.count(letter)==2:
                add_to_count2 = True
            if id_str.count(letter)==3:
                add_to_count3 = True
        count2+=add_to_count2
        count3+=add_to_count3
    print(count2*count3)

    for pair in itertools.combinations(ids,2):
        mismatchcount = 0
        id1, id2 = pair
        output = ""
        for i in range(len(id1)):
            if id1[i]!=id2[i]:
                mismatchcount+=1
            else:
                output = output + id1[i]
            if mismatchcount>1:
                break
        if mismatchcount==1:
            print(output)
            break


main()
