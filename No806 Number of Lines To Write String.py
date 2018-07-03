def numberOfLines(widths, S):
    char_width = dict(zip([chr(i) for i in range(97, 123)], widths))
    print(char_width)
    n = 1
    m = 100
    for i in range(len(S)-1):
        m -= char_width[S[i]]
        if m < char_width[S[i+1]]:
            m = 100
            n += 1
        else:
            continue
    return [n, 100-m+char_width[S[-1]]]