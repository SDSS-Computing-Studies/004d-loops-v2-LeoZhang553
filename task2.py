#! python3

#task2

N=(input("enter a name: ")).strip()
NameList = ("Lebron", "Kobe", "Michale", "Shaq", "Dennis")
a=0
for i in range(5):
    if NameList[i]==N:
        print('That name is on the list')
        a += 1
        continue
if a==0:
    print("That name is not on the list")