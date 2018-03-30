#Create a List called address
address=["Flat Floor Street","18","New York"];

#Create a Dictionary call Pins
pins={"Mike":1234,"Joe":1111,"Jack":2222};

#Print index 0 and index 1 of address
print(address[0],address[1]);

#Get an integer input from user
pin = int(input("Enter your pin: "));

#Create a function called find_in_file which takes a parameter f
def find_in_file(f):
    #Opens sample.txt
    myfile = open("sample.txt");

    #Reads the Whole File
    fruits= myfile.read();

    #Splits File by Line
    fruits = fruits.splitlines();

    #Checks if parameter f is in list fruits
    if f in fruits:
        return "That fruit is is in the list";
    else:
        return "No such fruit found";

#Check if enter pin is in values of pins
if pin in pins.values():
    #Gets a Fruit from user
    fruit = input("Enter Fruit: ");
    print(find_in_file(fruit));
else:
    print("Incorrect Pin");
    print("This info can only be accessed by:");
    for key in pins.keys():
        print(key)
