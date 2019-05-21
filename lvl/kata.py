def xp_to_target_lvl(current_xp=-1, target_lvl=-1):
    if not is_valid(current_xp, target_lvl):
        return "Input is invalid."

    exp = 314
    need = 314
    for i in range(2, target_lvl):
        exp = int(exp * (percent_for_lvl(i) + 1))
        need += exp

    res = need - current_xp
    if res <= 0 or target_lvl == 1:
        return "You have already reached level " + str(target_lvl) + "."
    else:
        return res


def is_valid(current_xp, target_lvl):
    return not (current_xp == -1 or
                target_lvl == -1 or
                not isinstance(current_xp, int) or
                not isinstance(target_lvl, int) or
                current_xp < 0 or
                target_lvl < 1 or
                target_lvl > 170)


def percent_for_lvl(lvl):
    return (25 - lvl // 10) / 100
