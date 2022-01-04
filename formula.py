a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите c "))

var1=((a**2+b**2)/(3*b-4))
var2=((4*c**5)/6)
rez=var1/var2
rez1=int(var1/var2)

print('Целая часть числа: ',rez1)
print('Остаток от деления: ',abs(rez1-rez))