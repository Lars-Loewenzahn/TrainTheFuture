
# 1! = 1
# 2! = 2*1    = 2 * 1!
# 3! = 3*2*1   = 3 * 2!
# 4! = 4*3*2*1 = 4 * 3!


def fact(n):
    if n < 2: 
        return 1
    else:
        return n*fact(n-1)

def fact2(n):
    if n >= 2:
        return n*fact(n-1)
    else:
        return 1

print(fact2(4))

### Gegeben: