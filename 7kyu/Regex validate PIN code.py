def validate_pin(pin):
    return pin.isnumeric() and (len(pin) == 4 or len(pin) == 6)


if __name__ == '__main__':
    print(validate_pin('1'))
    print(validate_pin('12'))
    print(validate_pin('123'))
    print(validate_pin('1234'))
    print(validate_pin('12345'))
    print(validate_pin('123456'))
    print(validate_pin('1a34'))
    print(validate_pin('-12345'))
    print(validate_pin('1.234'))
