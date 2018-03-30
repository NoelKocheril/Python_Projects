ln = input().split()
scores = []
output = []
if len(ln) != 2:
 # print("Usage: <Num of Contestants> <Num of Entries>");
  quit();
if((ln[0] < ln[1]) or (int(ln[1]) < 1)):
  #print("Number of Entries can not be greater than Number of Contestants");
  quit();
if((int(ln[0]) > 100000) or int(ln[0]) < 1):
  quit();
for i in range(0,int(ln[0])):
  scores.append(int(input()));
#print(scores);
scores.sort();
scores.reverse();
#print(scores);
for j in range(0,int(ln[1])):
  output.append(int(scores[j]));
#print(output);
print(sum(output));
