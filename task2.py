#! python3

#task2

N=(input("enter a name: ")).strip()
NameList = ("Guile", "Cammy", "Ryu", "Ken", "Chun-Li")
for i in range(5):
    if NameList[i]==N:
        print('yes')
    else:
        print("no")
        break
