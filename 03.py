import itertools


def load():
    with open("inputs/03.txt") as f:
        lines = f.read().strip()
        return lines.split("\n")

class Claim:
    def __init__(self, idnum, x, y, width, height):
        self.id = idnum
        self.x = int(x)
        self.y = int(y)
        self.w = int(width)
        self.h = int(height)
        self.overlap_count = 0

    def intersect_other_claim(self, c2):
        new_area = None
        x1 = max(self.x, c2.x)
        y1 = max(self.y, c2.y)
        x2 = min(self.x + self.w, c2.x + c2.w) - 1
        y2 = min(self.y + self.h, c2.y + c2.h) - 1
        if x1 <= x2 and y1 <= y2:
            new_area = Claim(0, x1, y1, x2-x1+1, y2-y1+1)
        return new_area

    def has(self, coord):
        x, y = coord
        return self.x <= x < self.x+self.w and self.y <= y < self.y + self.h

def main():
    claims = []
    for line in load():
        idnum, _,  xy, wh = line.split(" ")
        x, y = xy.strip(":").split(",")
        w, h = wh.split("x")
        new_claim = Claim(idnum.strip("#"), x, y, w, h)
        claims.append(new_claim)

    overlapping_areas = []
    for c1, c2 in itertools.combinations(claims, 2):
        # determine an overlapping region
        new_area = c1.intersect_other_claim(c2)
        if new_area:
            overlapping_areas.append(new_area)
            c1.overlap_count += 1
            c2.overlap_count += 1
    tile_list = set()
    for area in overlapping_areas:
        for x in range(area.x,area.x+area.w):
            for y in range(area.y,area.y+area.h):
                tile_list.add((x,y))
    print(f"part1: {len(tile_list)}")
    for claim in claims:
        if claim.overlap_count == 0:
            print(f"part2: {claim.id}")




    # slow search
    #for x in range(1000):
    #    print(x)
    #    for y in range(1000):
    #        claim_count = 0
    #        for claim in claims:
    #            if claim.has((x, y)):
    #                claim_count += 1
    #            if claim_count>1:
    #                overlapped += 1
    #                break
    #print(overlapped)


main()
