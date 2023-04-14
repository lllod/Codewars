def ip_to_int32(ip: str) -> int:
    ip_list_int2 = [bin(int(i))[2:] for i in ip.split('.')]
    for i in range(len(ip_list_int2)):
        if len(ip_list_int2[i]) < 8:
            diff = 8 - len(ip_list_int2[i])
            ip_list_int2[i] = ('0' * diff) + ip_list_int2[i]
    return int(''.join(ip_list_int2), 2)


if __name__ == '__main__':
    ip_address = '128.114.17.104'
    print(ip_to_int32(ip_address))
