# Задание 1
my_list = [6, 75, 505, 96, 159, 48, 851, 36, 759, 46]
for number in my_list:
    if number > 100:
        print(number)
####################################################
# Задание 2
my_list = [6, 75, 505, 96, 159, 48, 851, 36, 759, 46]
my_result = []
for num in my_list:
    if num > 100:
        my_result.append(num)
print(my_result)
####################################################
# Задание 3
my_list = [75, 525]
if len(my_list) >= 2:
    my_list.append(my_list[-2] + my_list[-1])
else:
    my_list.append(0)
print(my_list)
####################################################
# Задание 4
my_string = '0123456789'
num = ''.join(my_string)
num_1 = ''.join(my_string)
new_list = []
for x in num:
    for y in num_1:
        new_list.append(x + y)
print(new_list)