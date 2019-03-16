# https://www.codewars.com/kata/battleship-field-validator/train/python
def validate_battlefield(field):
    if [item for sublist in field for item in sublist].count(1) != 20:
        return False

    ship_d = find_all_ships(field)

    return ship_d[4] == 1 and ship_d[3] == 2 and ship_d[2] == 3 and ship_d[1] == 4


def find_all_ships(field):
    ships = {
        4: 0,
        3: 0,
        2: 0,
        1: 0
    }
    tuples_list = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]:
                tuples_list.append((i, j))

    for t in tuples_list:
        if not check_diagonal(t, field):
            return ships

    while len(tuples_list) != 0:
        res = [tuples_list[0]]
        res.extend(up(tuples_list[0], field))
        res.extend(down(tuples_list[0], field))
        res.extend(left(tuples_list[0], field))
        res.extend(right(tuples_list[0], field))
        for t in res:
            del tuples_list[tuples_list.index(t)]
        ships[len(res)] += 1

    return ships


def check_diagonal(point, field):
    check_points = [(point[0] + 1, point[1] + 1),
                    (point[0] + 1, point[1] - 1),
                    (point[0] - 1, point[1] + 1),
                    (point[0] - 1, point[-1] - 1)]
    t_list = list(filter(lambda x: 0 <= x[0] < 10 and 0 <= x[1] < 10, check_points))

    for t in t_list:
        if field[t[0]][t[1]]:
            return False

    return True


def up(x_t, field):
    res = []
    counter = 1
    while x_t[0] + counter < 10 and field[x_t[0] + counter][x_t[1]]:
        res.append((x_t[0] + counter, x_t[1]))
        counter += 1
    return res


def down(x_t, field):
    res = []
    counter = 1
    while x_t[0] - counter >= 0 and field[x_t[0] - counter][x_t[1]]:
        res.append((x_t[0] - counter, x_t[1]))
        counter += 1
    return res


def right(x_t, field):
    res = []
    counter = 1
    while x_t[1] + counter < 10 and field[x_t[0]][x_t[1] + counter]:
        res.append((x_t[0], x_t[1] + counter))
        counter += 1
    return res


def left(x_t, field):
    res = []
    counter = 1
    while x_t[1] - counter >= 0 and field[x_t[0]][x_t[1] - counter]:
        res.append((x_t[0], x_t[1] - counter))
        counter += 1
    return res
