# 最原始的方案
def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

# 重叠子问题：上述方案存在重叠子问题，导致大量重复计算，造成了大量计算重复，比如fib(20)=fib(19)+fib(18)，fib(19)=fib(18)+fib(17)，那么fib(18)就被计算了两次；
# 解决办法：备忘录；即带备忘录的递归算法来减少重复计算，直接查询；
def fib2(n):
    memo = [0]*n
    return sub_fib2(memo, n)

def sub_fib2(memo, n):
    print(memo)
    if n == 1 or n == 2:
        return 1
    else:
        if memo[n-1] == 0:
            memo[n-1] = sub_fib2(memo, n-1) + sub_fib2(memo, n-2)
        return memo[n-1]
