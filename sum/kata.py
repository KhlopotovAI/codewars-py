def sum_pairs(ints, s):
    mem = set()
    pairs = {}
    last_res_index = len(ints)
    for i in range(0, len(ints)):
        if ints[i] in mem:
            continue
        else:
            mem.add(ints[i])

        if i >= last_res_index:
            break

        index = None
        try:
            index = ints.index(s - ints[i], i + 1, last_res_index)
        except ValueError:
            pass
        if index:
            last_res_index = index
            pairs[index] = [ints[i], ints[index]]
    return pairs[min(pairs.keys())] if len(pairs) != 0 else None
