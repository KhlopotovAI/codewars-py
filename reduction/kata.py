# https://www.codewars.com/kata/directions-reduction/train/python
DIRECTIONS = {"NORTH": 0b0001, "SOUTH": 0b0010, "WEST": 0b0100, "EAST": 0b1000}
INV_DIRECTIONS = {v: k for k, v in DIRECTIONS.items()}
OPPOSITE = [0b0011, 0b1100]


def dirReduc(arr):
    binary_directions = list(map(lambda x: DIRECTIONS[x], arr))
    smart_path = list(map(lambda x: INV_DIRECTIONS[x], dir_reduce_binary(binary_directions)))
    return smart_path


def dir_reduce_binary(binary_arr):
    smart_list = []
    counter = 0
    while counter < len(binary_arr) - 1:
        if opposite(binary_arr[counter], binary_arr[counter + 1]):
            counter += 2
        else:
            smart_list.append(binary_arr[counter])
            counter += 1

    if counter == len(binary_arr) - 1:
        smart_list.append(binary_arr[counter])

    if len(binary_arr) != len(smart_list):
        return dir_reduce_binary(smart_list)
    else:
        return smart_list


def opposite(first, second):
    return first + second in OPPOSITE
