# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

my_list = [i**3 for i in range(1, 1001, 2)]
print(my_list)
final_sum = 0
for i in my_list:
    i += 17
    spec_sum = 0
    for num in str(i):
        spec_sum += int(num)
        if spec_sum % 7 == 0:
            final_sum += i
print(final_sum)

final_sum = 0
for i in my_list:
    spec_sum = 0
    for num in str(i):
        spec_sum += int(num)
        if spec_sum % 7 == 0:
            final_sum += i
print(final_sum)