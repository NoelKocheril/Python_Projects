src = [];
des = [];
src = input().split();
des = input().split();
energy = int(input());
#print(src);
#print(des);
#print(energy);
if(energy > 10000 or energy < 1):
  quit();
req = abs(int(des[0])-int(src[0])) + abs(int(des[1])-int(src[1]));
if((energy%2) != (req%2)):
  print("N");
elif(req > energy):
  print("N");
else:
  print("Y");
