def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    flag = True
    if word[0].islower():
        for i in range(1, len(word)):
            if word[i].isupper():
                flag = False
                break
            else:
                pass
    else:
        if len(word) == 1:
            return True
        elif word[1].islower():
            for i in range(1, len(word) - 1):
                if word[i].islower() and word[i + 1].islower():
                    continue
                else:
                    flag = False
                    break
        else:
            for i in range(1, len(word) - 1):
                if word[i].isupper() and word[i + 1].isupper():
                    continue
                else:
                    flag = False
                    break

    return flag
word = "FlaG"
print(detectCapitalUse(word))