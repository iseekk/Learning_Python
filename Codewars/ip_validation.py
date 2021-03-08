from socket import inet_pton, AF_INET, error


def ip_validation(string):
    try:
        inet_pton(AF_INET, string)
        return True
    except error:
        return False


if __name__ == '__main__':
    print(ip_validation("111.111.111.111"))
    print(ip_validation("111.256.111.111"))
    print(ip_validation("111.012.111.111"))