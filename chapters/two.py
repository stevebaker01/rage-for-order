from steves_utilities.profiler import profile


def p2_is_sorted_recursive(l):
    if len(l) < 2:
        return True
    return l[1] >= l[0] and p2_is_sorted_recursive(l[1:])


# return | ... WTF!
def p3_all_binary_sequences(n):
    these = ['0', '1']
    if n == 0:
        return ['']
    elif n == 1:
        return these
    else:
        for x in range(n - 1):
            those = []
            for y in these:
                those += [y + '0', y + '1']
            these =  those
        return these


@profile
def p5_find_largest_region_fill(m):

    # fill regions one at a time
    if not m:
        return 0
    region, regions, searched = ([], [], [],)
    rows, cols = (len(m), len(m[0]))
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def in_region(p):
        x, y  = p[0], p[1]
        if (x < 0 or x > rows - 1) or (y < 0 or y > cols - 1) or not int(m[x][y]):
            return
        if p in region or p in searched:
            return
        region.append(p)
        searched.append(p)
        for d in dir:
            adjacent = [x + d[0], y + d[1]]
            in_region(adjacent)

    for row in range(rows):
        for col in range(cols):
            this = [row, col]
            if this in searched:
                continue
            in_region([row, col])
            regions.append(len(region))
            region = []
    return max(regions)


@profile
def p5_find_largest_region_eval(m):

    # evaluate each cell against potentially all cells of known regions
    regions = []
    def place(p, regions):
        if not regions:
            return [[p]]
        mems = []
        for i in range(len(regions)):
            for x in regions[i]:
                if ((p[0] >= x[0] - 1) and (p[0] <= x[0] + 1)) and ((p[1] >= x[1] - 1) and (p[1] <= x[1] + 1)):
                    mems.append(i)
                    break
        if mems:
            merge = []
            for m in mems:
                merge += regions[m]
            merge += [p]
            v = [regions[x] for x in set(range(len(regions))).difference(set(mems))] + [merge]
            return v
        return regions + [[p]]

    for x in range(len(m)):
        for y in range(len(m[0])):
            if int(m[x][y]):
                regions = place([x,y], regions)
    return max([len(region) for region in regions])
