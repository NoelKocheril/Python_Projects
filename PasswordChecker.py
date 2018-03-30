correct_pass = "python123"
name = input("Enter Username: ");
password = input("Enter Password: ")
while (password != correct_pass):
    print("Incorrect Password, Please Try Again")
    password = input("Enter Password: ")
print("Hello %s, you are logged in" % name)
