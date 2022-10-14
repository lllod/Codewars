def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent / 100) + aug)
        year += 1
    return year


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000))
    print(nb_year(1500000, 2.5, 10000, 2000000))
    print(nb_year(1500000, 0.25, 1000, 2000000))
