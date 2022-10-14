def is_isogram(string):
    count = True
    for i in string.lower():
        if string.lower().count(i) > 1:
            count = False
            break
        else:
            count = True
    return count