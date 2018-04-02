def Calc_Length(f):
    if type(f)==int:
        return "Sorry Integers don't have length"
    elif type(f)==float:
        return "Sorry Float don't have length"
    return len(f)

test = "This is a test string"
print(Calc_Length(test))
test="thi"
print(Calc_Length(test))
# noinspection PyTypeChecker
print(Calc_Length(10))
# noinspection PyTypeChecker
print(Calc_Length(10.3))
