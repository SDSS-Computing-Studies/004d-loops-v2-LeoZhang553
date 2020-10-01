#problem2

#! python3

N=(input("input a number: ")).strip()
N=int(N)
a=1
for i in range(0,N):
    a *= N
    N -= 1
print(a)
