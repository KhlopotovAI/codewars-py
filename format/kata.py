# https://www.codewars.com/kata/human-readable-duration-format/train/python
intervals = (
    ('years', 31536000),  # 60 * 60 * 24 * 365
    ('days', 86400),  # 60 * 60 * 24
    ('hours', 3600),  # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)


def format_duration(seconds):
    if seconds == 0:
        return "now"
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))

    if len(result) > 1:
        return ", ".join(result[:-1]) + " and " + result[-1]
    else:
        return result[0]
