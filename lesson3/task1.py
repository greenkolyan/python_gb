numbers_eng_rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(eng_num):
    return numbers_eng_rus.get(eng_num)


eng_word = input('Введите число от 1 до 10 на английском: ')
print(num_translate(eng_word))
