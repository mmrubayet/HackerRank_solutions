cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0, 1]
    for i in range(2, n):
            l.append(l[i-1]+l[i-2])
    return l[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
# cube = lambda x: x * x * x
# print(list(map(cube, map(fib, range(int(input()))))))
