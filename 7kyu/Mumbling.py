def accum(s):
    return '-'.join([(s[i] * (i + 1)) for i in range(len(s))]).title()