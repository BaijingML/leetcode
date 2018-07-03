def judgeCircle(moves):
    a = moves.count('U') - moves.count('D')
    b = moves.count('R') - moves.count('L')
    if a == 0 and b == 0:
        return True
    else:
        return False

moves = "UD"
print(judgeCircle(moves))