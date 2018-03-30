f = open('fruits.txt');
fruits = f.read()
fruits = fruits.splitlines()
f.close()
for f in fruits:
    print(len(f))
