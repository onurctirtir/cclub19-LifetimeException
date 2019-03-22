
if __name__ == '__main__':

    string = list(input())
    N = int(input())

    l = []

    for _ in range(N):
        b, a = str(input()).split()
        l.append((b, a))

    for i in range(len(string)):
        for b, a in reversed(l):
            if string[i] == a:
                string[i] = b

    print(''.join(string))
