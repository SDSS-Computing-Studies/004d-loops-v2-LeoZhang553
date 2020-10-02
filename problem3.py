#problem 3

#! python3

N=input(("enter a integer: ")).strip()
N=int(N)
a=0
for i in range(0,N):
    c="1"*N
    c=int(c)
    a += c
    N -= 1
a=str(a)
print("the sum of the series is "+a)