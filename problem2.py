#problem2

#! python3

N=(input("input a number: ")).strip()
N=int(N)
C=N
a=1
for i in range(0,N):
    a *= N
    N -= 1
a=str(a)
C=str(C)
print(C+"!"+" is "+a)
