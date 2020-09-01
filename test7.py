import sys

n = int(sys.argv[1])

def fib(n):
    Fibo = []
    for num in range(0,n):
        if num <2:
            Fibo.append(1)
        else:
            Fibo.append(Fibo[num-1] + Fibo[num-2])
    return Fibo[num]
    
print(fib(n))



                                                                                   
