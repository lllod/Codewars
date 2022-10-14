def find_short(s):
    count = 100
    for i in s.split():
        if len(i) < count:
            count = len(i)
    return count