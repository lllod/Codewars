def friend(x):
    return [i for i in x if len(i) == 4 and i.isalpha()]


if __name__ == '__main__':
    print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
