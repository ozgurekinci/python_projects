if __name__ == '__main__':
    s = input()
    ismi = True
    for i in s:
        if i.isalnum():
            ismi = True
            break
        else:
            ismi = False
    print(ismi)

    ismi = True
    for i in s:
        if i.isalpha():
            ismi = True
            break
        else:
            ismi = False
    print(ismi)

    ismi = True
    for i in s:
        if i.isdigit():
            ismi = True
            break
        else:
            ismi = False
    print(ismi)

    ismi = True
    for i in s:
        if i.islower():
            ismi = True
            break
        else:
            ismi = False
    print(ismi)

    ismi = True
    for i in s:
        if i.isupper():
            ismi = True
            break
        else:
            ismi = False
    print(ismi)