def Cels_to_Faren(c):
    if(c < -273.15):
        return 'Temperature not Possible, Lowest Temperature is: -273.15'
    f = c * 9/5 + 32
    return f

lst = [10,-20,-289,100]
with open("output.txt",'w') as myfile:
    for e in lst:
        if e > -273.15:
            myfile.write(str(Cels_to_Faren(e))+'\n')
