my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for num in my_list:
    if num.isdigit():  # проверка на число
        new_list.extend(['"', f'{int(num):02d}', '"'])  # добавляем 0 впереди числа и кладем список в new_list
    elif (num.startswith('+') or num.startswith('-')) and num[1:].isdigit():  # если элемент начинается с + или - и делаем срез этого элемента с 1 позиции и до конца
        new_list.extend(['"', f'{num[0]}{int(num):02d}', '"'])
    else:
        new_list.append(num)

output = ' '.join(new_list)
print(output)
