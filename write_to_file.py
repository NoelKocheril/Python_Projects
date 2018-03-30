lst = [1,2,3]
f = open('out.txt', 'w')
for e in lst:
    f.write(str(e)+'\n')
f.close()
