my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in my_list:
    print('Привет!', name.split()[-1].title())
