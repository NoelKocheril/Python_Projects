def Cels_to_Faren(c):
    if(c < -273.15):
        return 'Temperature not Possible, Lowest Temperature is: -273.15'
    f = c * 9/5 + 32
    return f

# print(Cels_to_Faren(20))
# print(Cels_to_Faren(100))
# print(Cels_to_Faren(10))
# print(Cels_to_Faren(-273.15))
# print(Cels_to_Faren(-274))

lst = [10,-20,-289,100]
for e in lst:
    print(Cels_to_Faren(e))
