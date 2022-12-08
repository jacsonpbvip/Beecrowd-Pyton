a, b, c = str(input()).split()

a = float(a)
b = float(b)
c = float(c)

ab = a + b
ac = a + c
bc = b + c

if a < bc and b < ac and c < ab :
    perimetro = a + c + b
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))