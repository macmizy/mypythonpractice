def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
if __name__ == "__main__":
    x = int(input("input your value"))
    result1 = fact(x)
    print(result1)
    print("using recursion")

def factorial (n):
    if n == 0:
        return 1
    return n * fact(n-1)

a = int(input("input your value"))
result2 = fact(a)


