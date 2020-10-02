W=(input("enter width: ")).strip()
H=(input("enter height: ")).strip()
W=int(W)
H=int(H)
for i in range(0,W):
    print('*',end='')
print("\n")
for i in range(0,H-2):
    print("*",end="")
    S=" "
    print(S*(W-2),end="*")
    print('\n')
for i in range(0,W):
    print('*',end='')