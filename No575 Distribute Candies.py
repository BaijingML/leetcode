def distributeCandies(candies):
    a = len(set(candies))
    b = int(len(candies)/2)
    if  b <= a:
        return b
    else:
        return a

print(distributeCandies([1,1,2,3]))