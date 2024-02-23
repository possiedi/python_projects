def multiple(mult):
    def calc(user_number):
        return mult * user_number
    return calc

double = multiple(2)
triple = multiple(3)
quadruple = multiple(4)

print(double(5))
print(triple(7))
print(quadruple(2))
