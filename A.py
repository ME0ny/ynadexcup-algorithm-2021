'''
    Задача 1 Yandex cup 2021
'''

a = input()
b = input()

ab=""
bb=""
while (len(a) > 0):
    if (a[0] == 'o'):
    	ab += "1"
    	a = a[3:]
    else:
        ab += "0"
        a = a[4:]
while (len(b) > 0):
    if (b[0] == 'o'):
    	bb += "1"
    	b = b[3:]
    else:
    	bb += "0"
    	b = b[4:]
a = int(ab, 2)
b = int(bb, 2)
if (a > b):
	print(">")
elif (a < b):
	print("<")
else:
	print("=")
