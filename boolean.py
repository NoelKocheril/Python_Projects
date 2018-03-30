import sys;
sentence = input().split();
count = 0;
for word in sentence:
  #print(word)
  if(word.lower() == "not"):
    count = count+1;
#print(count);
if(sentence[-1].lower() == "true"):
  final = True;
  if(count%2==1):
    final = not final;
  #print("Final boolean:", final);
  print(final);
elif(sentence[-1].lower() == "false"):
  final = False;
  if(count%2==1):
    final = not final;
  #print("Final boolean:", final);
  print(final);
else:
  print("Not a valid structure");
  print("Usage: <* true/false>");
  sys.exit(1);
