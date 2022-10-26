for i in range(10):
    print(i)
    i += 8


def get_all(char, list_of_chars) -> int:
    # return amount of chars that follow supplied
    print(list_of_chars)
    amount = 0
    for i in list_of_chars:
        if char == i:
            amount += 1
        else:
            break
    return amount - 1


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


if __name__ == '__main__':
    print(get_all('a', convert('abc')))
    print(get_all('a', convert('aaasadsa')))
