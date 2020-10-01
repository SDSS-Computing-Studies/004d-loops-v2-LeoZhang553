#! python3

#task1

N=(input("enter a number: ")).strip()
N=int(N)
for a in range(1,13):
    a=int(a)
    c=N*a
    print(c,end=" ")
