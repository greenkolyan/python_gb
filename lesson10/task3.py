class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сложение ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return 'Вычитание ' + str(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Вычитание невозможно'

    def __mul__(self, other):
        return 'Умножение ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Деление ' + str(round(self.nums / other.nums))


cell_1 = Cell(56)
cell_2 = Cell(28)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1.make_order(10), '\n')
print(cell_2.make_order(10), '\n')

