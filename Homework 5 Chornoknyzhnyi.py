#Задание №1
a = int(input('Your number:'))
z = 0
for i in range(len(a)):
  if a[i] == '0':
    z = z + 1
print(z)
# n = int(input())
#
# if (n == 0):
#     print(1)
#     exit()
#
# countZero = 0
# while (n % 10 == 0):
#     n //= 10
#     countZero += 1
#
# print(countZero)
###########
#Задание №2
# my_value = int(input('Your number:'))
# zero = 0
# while my_value % 10 == 0:
#     zero += 1
#     my_value //= 10
# print(zero)