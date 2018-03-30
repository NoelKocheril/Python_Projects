Temp = input("")
N = int(input("Enter Number of Guest: "))
names = []
for i in range(N):
  names.append(input())
# print(names)C
for name in names:
  print(Temp.replace(">",name))
