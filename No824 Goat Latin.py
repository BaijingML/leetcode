def toGoatLatin(self, S):
    """
    :type S: str
    :rtype: str
    """
    vowel = 'aeiouAEIOU'
    a = S.split(' ')
    for i in range(len(a)):
        if a[i][0] in vowel:
            a[i] = a[i] + 'ma' + 'a' * (i + 1)
        else:
            a[i] = a[i][1:] + a[i][0] + 'ma' + 'a' * (i + 1)
    return ' '.join(a)