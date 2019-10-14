# def minion_game(string):
#     # your code goes here
#     # stuart = 0
#     # kevin = 0
#     kevin, stuart = [0,0]
#     vowels = "AEIOU"
#     rangee = range(len(string))
#     # rangeep1 = (i+1,len(string)+1)
#     kevstu = [j for i in rangee for j in range(i+1,len(string)+1) if s[i] in vowels ]
#     for i in rangee:
#         for j in range(i+1,len(string)+1):
#             if string[i] in vowels:
#                 kevin += 1
#             else:
#                 stuart += 1
#     if kevin < stuart:
#         print("Stuart", stuart)
#     elif kevin > stuart:
#         print("Kevin", kevin)
#     else:
#         print("Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = "AEIOU"
    rangee = len(string)
    # rangeep1 = (i+1,len(string)+1)
    for i in string:
        for j in string[:len(string)]:
            if i in vowels:
                kevin += 1
            else:
                stuart += 1
    if kevin < stuart:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
