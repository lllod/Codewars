def maskify(cc):
    return '#' * len(cc[:-4]) + cc[-4:]


if __name__ == '__main__':
    print(maskify('4556364607935616'))