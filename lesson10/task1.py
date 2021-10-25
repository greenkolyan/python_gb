class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Проблемы с формой'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Проблемы с формой'
        return answer


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_4 = Matrix([[8, 14, 6], [13, -6, 9], [4, -7, 26]])
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_3, '\n')
print(matrix_4, '\n')
print(matrix_1 + matrix_3)
print(matrix_2 + matrix_4)

