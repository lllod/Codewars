def longest(a1, a2):
    set1 = set(a1)
    set1.update(set(a2))
    return ''.join(sorted(set1))


if __name__ == '__main__':
    print(longest("aretheyhere", "yestheyarehere"))
    print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
    print(longest("inmanylanguages", "theresapairoffunctions"))
