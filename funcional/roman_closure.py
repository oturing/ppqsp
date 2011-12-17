
def to_roman():

    romanNumeralMap = (
        ('M',  1000), ('CM', 900), ('D',  500), ('CD', 400), ('C',  100), ('XC', 90),
        ('L',  50), ('XL', 40), ('X',  10), ('IX', 9), ('V',  5), ('IV', 4), ('I',  1))

    def _to_roman(n):
        result = ''
        for numeral, integer in romanNumeralMap:
            while n >= integer:
                result += numeral
                n -= integer
        return result
    return _to_roman

to_roman = to_roman()
for i in range(1, 21):
    print to_roman(i)