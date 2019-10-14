import string

def print_rangoli(size):
    list = [x for x in string.ascii_lowercase[:size]]
    list_ = list[::-1]
    if size == 1:
        print("a")
    else:
        for i in range(1,len(list_)+1):
            print(("-".join(list_[:i]) + "-" + "-".join(list[(len(list)-i+1):])).center(4*size-3,"-"),sep="-")
        for i in range(len(list_),1,-1):
            print(("-".join(list_[:i-1]) + "-" + "-".join(list[(len(list)-i+2):])).center(4*size-3,"-"),sep="-")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)