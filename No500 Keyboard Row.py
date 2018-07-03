def findWords(words):
    firstline = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    secondline = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    thirdline = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    line = []
    for i in words:
        k = i.lower()

        if k[0] in firstline:
            flag = 1
            for j in k[1:]:
                if j not in firstline:
                    flag = 0
                    break
            if flag == 1:
                line.append(i)
        elif k[0] in secondline:
            flag = 1
            for j in k[1:]:
                if j not in secondline:
                    flag = 0
                    break
            if flag == 1:
                line.append(i)
        else:
            flag = 1
            for j in k[1:]:
                if j not in thirdline:
                    flag = 0
                    break
            if flag == 1:
                line.append(i)
    return line