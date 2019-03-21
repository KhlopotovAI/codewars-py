def solution(string, markers):
    lines = string.split("\n")

    def strip_line(line):
        res = line
        for marker in markers:
            res = res[:res.find(marker) if res.find(marker) != -1 else len(res)]
        return res.strip()

    return "\n".join(map(strip_line, lines))
