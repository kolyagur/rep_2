s1 = input("Введете строку s1")
s2 = input("Введете строку s2")

print (f'Вы ввели строку {s1} и {s2}')
print(F'Их длина соответствует {len(s1)} и {len(s2)}')
print (f'Первый символ первой строки: {s1[0]}')
print (f'Последний символ последней строк: {s2[len(s2)-1]}')
print(s1 == s2)
print(F's1 содержится в s2 {s1 in s2}')
print(F's2 содержится в s1 {s2 in s1}')