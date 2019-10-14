import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    while True:
        S = input()
        if 0 < len(S) < 1000:
            break
    while True:
        w = int(input())
        if 0 < w < len(S):
            break

print(wrap(S,w))