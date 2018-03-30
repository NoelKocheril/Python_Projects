dictionary = {};
i_dictionary = {};
text = "";
temp = "";

def inDictionary(w):
  if w in dictionary:
    return True;
  return False;

def addToDictionary(w):
  dictionary[w] = len(dictionary) +1;

def invert_dict(d):
    return dict([ (v, k) for k, v in d.items( ) ])
  
while True:
  temp = "";
 
  
  while(temp != "1" and temp != "2" and temp != "3" and temp != "4"):
    print();
    print("1. Look up Word in Dictionary and find Entry Number.");
    print("2. Look up Entry Number and Find Word.");
    print("3. Add more Words to the Dictionary.");
    print("4. Exit");
    temp = input();
  if(temp == "1"):
    text = input("Enter the Word you would like to find.\n");
    print(dictionary.get(text, "No such Key Exists."));
  elif(temp == "2"):
    while True:
      try:
        number = int(input("Enter the Entry Number."));
      except ValueError:
        print("Please Type a Number");
        continue;
      else:
        break;
    print(i_dictionary.get(number, "No word with the Entry Number."));
  elif(temp == "3"):
    text = input("Enter the Phrase you would like to add to the Dictionary\n").upper();
    text = text.split();
    for word in text:
      if inDictionary(word):
        print(dictionary[word], end=" ");
      else:
        print(word,end=" ");
        addToDictionary(word);
    i_dictionary = invert_dict(dictionary);
  else:
    break;
 
  
