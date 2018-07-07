def findLUSlength(self, a, b):
    if a != b:
        return max(len(a), len(b))
    else:
        return -1