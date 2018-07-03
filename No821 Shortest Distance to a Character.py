def shortestToChar(S, C):
    INF = 0x7FFFFFFF
    N = len(S)
    ans = [INF] * N
    lastC = -INF
    for i in range(N):
        if S[i] == C:
            lastC = i
        ans[i] = min(ans[i], i - lastC)

    lastC = INF
    for i in range(N - 1, -1, -1):
        if S[i] == C:
            lastC = i
        ans[i] = min(ans[i], lastC - i)
    return ans

print(shortestToChar("loveleetcode", 'e'))