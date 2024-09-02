from django.test import TestCase

# Create your tests here.

data = '12/15/1975'
print(data[6:])
if len(data) != 10:
    print('formato invalido')

print(len(data))
if data > '12':
    print('data invalida')

