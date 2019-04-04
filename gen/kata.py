# https://www.codewars.com/kata/check-the-status-of-the-generator-expression/train/python
def check_generator(gen):
    if not gen.gi_frame:
        return "Finished"
    if len(gen.gi_frame.f_locals) == 1:
        return "Created"
    return "Started"
